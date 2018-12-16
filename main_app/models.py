from django.db import models
from main_app.choices import *

# Create your models here.
class Resume(models.Model):
    resume = models.FileField(upload_to='resumes/%Y/%m/%d')
    username = models.CharField(max_length=150,default='someone')

# Profile model
class Profile(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    university = models.CharField(max_length=150, choices=UNIVERSITY_CHOICES)
    degree = models.CharField(max_length=150, choices=DEGREE_CHOICES)
    principles_foundations = models.BooleanField(blank=True)
    technology_enablers = models.BooleanField(blank=True)

