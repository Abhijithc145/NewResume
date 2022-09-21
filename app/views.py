from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json    
import re 
from .models import *
from .serializer import *
import ast
import math

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
        secondemails =0
        f = open('app/Shahin.json')
        data = json.load(f)
        datas = data['resumes'][0]['data']
        name = datas['name']['raw']
        location = datas['location']['state']
        tttt =0
        personemails=0
        if datas['emails']==[]:
            try:
                for i in range(0,len(datas['sections'])):
                    print(len(datas['sections'][i]))
                    if secondemails == 0 or secondemails == []:
                        
                        if datas['sections'][i]['sectionType'] == "PersonalDetails":
                            tttt=datas['sections'][i]['text']
                            secondemails= re.findall( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', tttt)
                            if secondemails != 0 or secondemails != []:
                                print(secondemails,"llllllllllllllllllllllllllllllllllllllllllll")
                                personemails = secondemails
                            else:    
                                print(secondemails,"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
                                
                        else:
                            print("Its not comming.................")    
                    else:
                        break
                    #     print(tttt)
                    #         print(secondemails,"ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                    #         personemails = secondemails 
                    #     else:    
                    #         print("llllll")  
                                
            except:
                print(personemails,"111111111111111111111111111111111111111111111")

                personemails = ["nodata"]


            
            
        else :
            personemails = datas['emails']
            
            

        try:
            experience= datas['totalYearsExperience'].exits

        except:
            experience=0
        try:
            phonenumber = datas['phoneNumbers'][0].exits

        except:
            phonenumber="No phone number"

        try:
            address=datas['location']['formatted'].exits
        except:
            address="No address "

        
        for i in range(0,len(datas['websites'])):
            websites.append(datas['websites'][i])
        
        
        for i in range(0,len(datas['education'])):
            education.append(datas['education'][i]['accreditation']['inputStr'])

        for i in range(0,len(datas['languages'])):
            language.append(datas['languages'][i])

        for i in range(0,len(datas['skills'])):
            skills.append(datas['skills'][i]['name']) 
        try:      
            print(personemails,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            Candidate.objects.create(firstname=name,address=address,skills=skills,education=education,locations=location,personemails=personemails[0],phonenumber=phonenumber,language=language,experions=experience,websites=websites)
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
        skillcount = 0
        locationcount=0
        educationcount=0
        experionscount = 0
        locationcount =0
        locationTrue = "No"
        companyexperionscount = 0
        companyeducationcount=0
        companyskillcount = 0


        average = 0
        Company = JobType.objects.all()
        Companyserilizer =dataserilaizer(Company,many=True)
        companyskill = Companyserilizer.data[0]['skills']
        companyskill1=ast.literal_eval(companyskill)
        companyeducation = ast.literal_eval(Companyserilizer.data[0]['education'])
        companyexperions = ast.literal_eval(Companyserilizer.data[0]['experions'])
        companylocation=Companyserilizer.data[0]['locations']
        companylocationcount=len(Companyserilizer.data[0]['locations'])
        
        companyexperions=companyexperions[0]
        
         


        Candidates = Candidate.objects.all()
        Candidateserilizer =candidateserilaizer(Candidates,many=True)


        for i in range(0,len(Candidateserilizer.data)): 
            for k in range(0,len(companyskill1)):
                datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
                for l in range(0,len(datas)):
                    value = datas[l]
                    if companyskill1[k].lower() == value[0:len(companyskill1[k])].lower():             
                        skillcount=skillcount+1


            for k in range(0,len(companyeducation)):
                datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
                for l in range(0,len(datas)):
                    value = datas[l]    
                    if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
                        educationcount = educationcount +1
                              
            if Candidateserilizer.data[i]['experions'] >= companyexperions:

                experionscount =  companyexperions
            else:
                experionscount =  Candidateserilizer.data[i]['experions']
            
            if companylocation == Candidateserilizer.data[i]['locations']:
                locationcount=locationcount+1
                locationTrue = "yes"
            else:
                locationcount=0
                locationTrue= 'NO'

            #company 
            companyskillcount = len(companyskill1)
            companyeducationcount = len(companyeducation)
            companyexperionscount= int(companyexperions)
            

            # Candidate
            candidateskillcount = skillcount
            candidateeducationcount = educationcount
            candidateexperionscount= int(experionscount)
            # print(candidateskillcount,candidateeducationcount,candidateexperionscount)
            


            Result = ((((candidateskillcount/companyskillcount)+(locationcount/1)+(candidateeducationcount/companyeducationcount)+(candidateexperionscount/companyexperionscount))/4)*100)
            Result="{:.1f}".format(Result)
         
        





        # print((((4/7)+1+(5/10)+(2/2))/4)*100)   

        

            print("------------------------------The--Datas----------------------------------------------------")
            print("")
            print("              Name   ",Candidateserilizer.data[i]['firstname'])
            print('')
            print('              education count',educationcount) 
            print('              skill count',skillcount)
            print('              experions count',experionscount)
            print('              Location',locationTrue)
            print()
            print("              percentage  :",Result,"%")
            print()
            
            # Matchdata.objects.create(name = name,skills=skillcount,education=educationcount)
            skillcount = 0
            educationcount = 0
            experionscount = 0





        return Response(Candidateserilizer.data,status=status.HTTP_200_OK)
        






