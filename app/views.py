from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json    
import re 
from .models import *
# Create your views here.

class Datas(APIView):
    print("llllllllllllllllllllllllllllllllllllllllllllllllll7888l")
    def get(self,request):
        skills=[]
        language=[]
        education =[]
        websites = []
        # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        f = open('app/data1.json')
        data = json.load(f)
        datas = data['resumes'][0]['data']
        name = datas['name']['raw']
        personemails = datas['emails']
        phonenumber = datas['phoneNumbers'][0]
        experience= datas['totalYearsExperience']
        
        for i in range(0,len(datas['websites'])):
            websites.append(datas['websites'][i])
        print(websites)
        
        for i in range(0,len(datas['education'])):
            education.append((datas['education'][i]['accreditation']['education'],datas['education'][i]['organization']))

        for i in range(0,len(datas['languages'])):
            language.append(datas['languages'][i])

        for i in range(0,len(datas['skills'])):
            skills.append(datas['skills'][i]['name'])   
        
        Candidate.objects.create(firstname=name,skills=skills,education=education,personemails=personemails[0],phonenumber=phonenumber,language=language,experions=experience,websites=websites)
        # print(Person.objects.all(()))

        

        
        
                
        return Response(datas,status=status.HTTP_200_OK)