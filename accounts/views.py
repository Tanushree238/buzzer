from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime, timedelta
import pytz

# Create your views here.

def login_page(request):
    post_data = request.POST or None
    if post_data:  
        username = post_data.get("username")
        name = post_data.get("name")
        password = post_data.get("password")
        user_obj = authenticate( request, username=username, password=password)
        if user_obj:
            login(request, user_obj )
            messages.success(request, 'Login successful!')
            if user_obj.is_superuser:
                return redirect('admin')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Incorrect Password.')
            return redirect('login')
    return render(request,"login.html",{'title':"Login"})


@staff_member_required
def admin_page(request,ques_id=None, *args, **kwargs):
    last_ques = Question.get_last_question()
    buzzer_start = False
    duration =""
    if last_ques:
        ques_count = last_ques.id
        if not last_ques.end_time:
            buzzer_start = True
            duration = (datetime.now() - last_ques.start_time.replace(tzinfo=None)).total_seconds()
        else:
            ques_count+=1   
    else:
        ques_count = 1
    if ques_id:
        buzzer_log_objs = BuzzerLogs.objects.filter(ques_id=ques_id).all()
    else:
        buzzer_log_objs = BuzzerLogs.objects.all()
    buzzer_logs = []
    count = 1
    tz = pytz.timezone("Asia/Calcutta")
    for buzzer_log_obj in buzzer_log_objs:
        log={}
        log['sno']=count 
        log['username']=buzzer_log_obj.user.username.upper()
        log["timestamp"]=(buzzer_log_obj.timestamp.replace(tzinfo=None)+timedelta(hours=5,minutes=30)).strftime("%b %d, %I:%M:%S %p")
        log["ques_id"]=buzzer_log_obj.ques_id
        log["name"]=buzzer_log_obj.name
        count+=1
        buzzer_logs.append(log)
    questions = [i for i in range(1,ques_count+1)]
    return render(request,"admin.html",{'title':"Admin", "ques_count":ques_count, "buzzer_start": buzzer_start, "duration":duration,"buzzer_logs":buzzer_logs,"questions":questions })


def buzzer_start(request, ques_no, *args, **kwargs):
    ques_obj = Question.objects.create(start_time=datetime.now())
    return redirect('admin1', ques_id = ques_no)


def buzzer_end(request, ques_no, *args, **kwargs):
    ques_obj = Question.objects.filter(id = ques_no).first()
    ques_obj.end_time = datetime.now()
    ques_obj.save()
    return redirect("admin1", ques_id = ques_no)


def home_page(request, *args, **kwargs):
    last_ques = Question.get_last_question()
    if last_ques:    
        ques_count = last_ques.id  
        if last_ques.end_time:
            ques_count+=1
    else: 
        ques_count = 1  
    return render(request,"home.html",{'ques_count':ques_count,'title':"Home"})


def press_buzzer(request, name, *args, **kwargs):
    last_ques = Question.get_last_question()
    if last_ques :
        if not last_ques.end_time:
            buzzer_log_obj = BuzzerLogs.objects.create(user_id=request.user.id,ques_id = last_ques.id, name=name,timestamp = datetime.now() )
        else:
            buzzer_log_obj = BuzzerLogs.objects.create(user_id=request.user.id, name=name,timestamp = datetime.now() )
    else:
        buzzer_log_obj = BuzzerLogs.objects.create(user_id=request.user.id, name=name,timestamp = datetime.now() )
    return redirect("home")


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect('login')