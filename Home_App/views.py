from django.shortcuts import render
from .models import Personal, Statistics, ProgrammingSkils, Certificates, SocialMedia, SendEmail, MyImage, Project

def show_home(request):
    if request.method == "POST":
        Name_get = request.POST.get('Name') 
        Email_get = request.POST.get('Email') 
        Subject_get = request.POST.get('Subject') 
        Message_get = request.POST.get('Message')      
        SendEmail.objects.create(Name= Name_get, Email= Email_get, Subject= Subject_get, Message= Message_get)
    
    Personal_info = Personal.objects.all() 
    Statistics_info = Statistics.objects.all()
    ProgrammingSkils_info = ProgrammingSkils.objects.all()
    Certificates_info = Certificates.objects.all()
    SocialMedia_info = SocialMedia.objects.all()
    MyImage_info = MyImage.objects.all()
    Project_info = Project.objects.all()
    
    return render(request, 'Home_App/index.html', {"Personal_info": Personal_info,
                                                   "Statistics_info": Statistics_info,
                                                   "ProgrammingSkils_info": ProgrammingSkils_info,
                                                   "Certificates_info": Certificates_info,
                                                   "SocialMedia_info": SocialMedia_info,
                                                   "MyImage_info": MyImage_info,
                                                    "Project_info": Project_info
                                                    }
                  )
    
    
def error(request, exception):
    return render(request, 'Home_App/404.html', {}, status=404)
        

