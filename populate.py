from django.contrib.auth import get_user_model

User = get_user_model()

users = {
    "D2" : {"Chiranjeev Khurana@892",
            "Shubham Singla@261iuhtfd", 
            "Chanchal Dhawan@30mnjh12", 
            "Ankit Kochar@674wsfgbhj", 
            "Arnav Bharadwaj@77mjnkiu8", 
            "Abhay Dhillon@347yuhjb53", 
            "Harsh Rao@346klla7", 
            "Chetan Chauhan@97sdsdd5"
            },
    "P1" : {"Kanchi Rajput@66sdsn7",
            "Sukhmanjot Singh@39adasf0",
            "Abhishek Janagal@5789vvfds",
            "Lalit Kanoria@49pcdoiyn3",
            "Deepak Tewatia@47379gvcs5",
            "Ramandeep Kamboj@8933s47",
            "Retika Bhat@4380rghbj23",
            "Riya Gupta@00hilp9292822",
            "Ashish Goyal@0202bkmld1443",
            "Jayant Garg@73d3455404jj",
            "Harsh Yadav@ubsdjds9333"
            },
    'Mentors' : {"Admin@9466201496aA38z950",}
}


for team, members in users.items():
    for member in members:
        name = member.split("@")[0] 
        if team == "Mentors":
            mem_obj = User.objects.create(username=name+"|"+team, password = member, is_superuser=True)
        else:
            mem_obj = User.objects.create(username=name+"|"+team, password = member)
        print(name,"'s entry done in user table")
