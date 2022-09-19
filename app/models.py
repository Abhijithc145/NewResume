from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    skills = models.CharField(max_length=1000)
    education = models.CharField(max_length=500)
    experions = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100,unique=True)
    personemails = models.CharField(max_length=100,unique=True)
    
