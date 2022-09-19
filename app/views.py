from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json    
import re 
from .models import *
from .serializer import *


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

class Datas(APIView):
    print("llllllllllllllllllllllllllllllllllllllllllllllllll7888l")
    def get(self,request):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        skills=[]
        language=[]
        education =[]
        websites = []
        f = open('app/Resume1.json')
        data = json.load(f)
        datas = data['resumes'][0]['data']
        name = datas['name']['raw']
        personemails = datas['emails']

        try:
            experience= datas['totalYearsExperience'].exits

        except:
            experience="No Experience"
        try:
            phonenumber = datas['phoneNumbers'][0].exits

        except:
            phonenumber="No phone number"

        try:
            address=datas['location']['formatted'].exits()
        except:
            address="No address "


        for i in range(0,len(datas['websites'])):
            websites.append(datas['websites'][i])
        
        
        for i in range(0,len(datas['education'])):
            education.append((datas['education'][i]['accreditation']['education'],datas['education'][i]['organization']))

        for i in range(0,len(datas['languages'])):
            language.append(datas['languages'][i])

        for i in range(0,len(datas['skills'])):
            skills.append(datas['skills'][i]['name']) 
        try:      
        
            Candidate.objects.create(firstname=name,address=address,skills=skills,education=education,personemails=personemails[0],phonenumber=phonenumber,language=language,experions=experience,websites=websites)
            return Response(datas,status=status.HTTP_200_OK)
        except:
            return Response({'Error':'The Email address or Phone number is already added in  another resumes .....! ,please Checkit......'})
            
 
        
class Addjobs(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = JobType.objects.all()
    serializer_class = dataserilaizer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)   

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)  


class Checkdata(APIView):
    def get(self,request):
        count = 0
        Company = JobType.objects.all()
        Companyserilizer =dataserilaizer(Company,many=True)

        Candidates = Candidate.objects.all()
        Candidateserilizer =candidateserilaizer(Candidates,many=True)
        print(Candidateserilizer.data[0]['language'])
        
        
        # for i in range(0,(len(Companyserilizer.data))):
        #     for j in range(0,len(Candidateserilizer.data)):
        #         Checkskill =Candidateserilizer.data[j]['language']
        #         try:
        #             print(len(Checkskill))
                
        
        #         except:
        #             print("data")    
        




     

        return Response(Candidateserilizer.data,status=status.HTTP_200_OK)
    

    

                
                