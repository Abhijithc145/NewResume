from operator import mod
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    personemails = models.CharField(max_length=100,unique=True)
    phonenumber= models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=500)
    education = models.CharField(max_length=500)
    skills = models.CharField(max_length=1000)
    experions = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    websites = models.CharField(max_length=1000)
    education = models.CharField(max_length=500)


class JobType(models.Model):
    skills = models.CharField(max_length=500)
    locations = models.CharField(max_length=100)
    education = models.CharField(max_length=500)
    experions = models.CharField(max_length=100)



class Matchdata(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    locations = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    experions = models.CharField(max_length=100)

       
