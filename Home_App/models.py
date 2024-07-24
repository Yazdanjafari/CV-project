from django.db import models
from django.utils import timezone

SocialMedia_choise =[ 
('instagram', 'instagram'),
('telegram', 'telegram'),
('linkedin', 'linkedin'),
('github', 'github'),
('whatsapp', 'whatsapp'),
('twitter-x', 'twitter-x'),
('youtube', 'youtube'),
('threads', 'threads'),
] 

Show_Side_skills =[ 
('Right', 'Right'),
('Left', 'Left')
] 

class Personal(models.Model):
    First_Name  = models.CharField(max_length= 55)
    Last_Name  = models.CharField(max_length= 55)
    Birthday = models.DateField()
    Age = models.IntegerField()
    Website = models.CharField(max_length= 55)
    City = models.CharField(max_length= 55)
    Email = models.CharField(max_length= 55)
    Short_Description = models.CharField(max_length= 255)
    Long_Description = models.CharField(max_length= 555)
    

class Statistics(models.Model):
    Happy_Clients = models.IntegerField()
    Projects = models.IntegerField()
    Job_history_in_years = models.IntegerField()
    Awards = models.IntegerField()
    
class ProgrammingSkils(models.Model):    
    Name = models.CharField(max_length= 55)
    How_Profotional = models.IntegerField()
    Show_Side = models.CharField(max_length= 55, choices= Show_Side_skills)
    def __str__(self):
        return self.Name
    
class Certificates(models.Model):
    Name = models.CharField(max_length= 55)
    Image = models.ImageField(upload_to="dinamic_img")
    def __str__(self):
        return self.Name

class SocialMedia(models.Model):
    Name = models.CharField(max_length= 55, choices= SocialMedia_choise)
    Link = models.CharField(max_length= 255)
    def __str__(self):
        return self.Name
    
class SendEmail(models.Model):
    Name = models.CharField(max_length= 255) 
    Email = models.CharField(max_length= 255)
    Subject = models.CharField(max_length= 255)
    Message = models.CharField(max_length= 255)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Subject : {self.Subject}"
    
    
class MyImage(models.Model):
    Image = models.ImageField(upload_to="dinamic_img")
    def __str__(self):
        return self.Image.url    
    
class Project(models.Model):
    Name = models.CharField(max_length= 55)
    Image = models.ImageField(upload_to="dinamic_img")    
    Link = models.CharField(max_length= 255, default="#")
    def __str__(self):
        return self.Name    
    
    
    
    
    