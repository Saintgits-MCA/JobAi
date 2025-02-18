from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
# from fields import ComparableMixin
from pip._internal import locations

class Jobseeker_Registration(models.Model):
    name=models.CharField(max_length=255,default="Unknown")
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class jobseeker_profile(models.Model):    
    user = models.OneToOneField(Jobseeker_Registration, on_delete=models.CASCADE, related_name='profile',null=True)  # ForeignKey to Jobseeker_Registration
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.CharField(max_length=50, blank=True, null=True)
    highest_qualification = models.CharField(max_length=255, blank=True, null=True)
    job_preference = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Jobseeker"

class jobseeker_resume(models.Model): 
    user = models.ForeignKey(Jobseeker_Registration, on_delete=models.CASCADE, null=True, blank=True)  # user is required, cannot be null
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Document uploaded by {self.user.username} on {self.uploaded_at}"
class Company_Type_Master(models.Model):
    company_type=models.CharField(max_length=50)
    def __str__(self):
        return self.name if self.name else "Unnamed Company"
    
class Company(models.Model):
    password=models.CharField(max_length=255)
    # Links to Django's built-in User model
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    company_type = models.ForeignKey(Company_Type_Master,on_delete=models.CASCADE,default=None)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class job_title(models.Model):
    job_title=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.name 
    
class company_joblist(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
    job_title = models.ForeignKey(job_title,on_delete=models.CASCADE,default=None)
    job_number = models.CharField(max_length=100)
    job_description = models.CharField(max_length=5000, blank=True, null=True)
    job_type = models.CharField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=200,null=True)
    highest_qualification = models.CharField(max_length=255, blank=True, null=True)
    skills_required = models.TextField(blank=True, null=True)
    dateofpublish=models.DateField(max_length=20,null=True)
    Lastdate=models.DateField(max_length=20,null=True)
    def __str__(self):
        return self.name 
    

    
class ResumeDetails(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    highest_qualification = models.CharField(max_length=255, blank=True, null=True)
    job_preference = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unknown Resume"


# class UserSettings(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
#     dark_mode = models.BooleanField(default=False)  # Dark Mode Setting
#     email_notifications = models.BooleanField(default=True)
#     two_factor_auth = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Settings for {self.user.username}"

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)