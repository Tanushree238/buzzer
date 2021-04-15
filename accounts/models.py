from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank = True, null=True)

    @staticmethod
    def get_last_question():
        question = Question.objects.order_by("-id").first()
        return question

class BuzzerLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ques = models.ForeignKey(Question, on_delete=models.CASCADE,blank = True, null=True)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
