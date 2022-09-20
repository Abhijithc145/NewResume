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
        f = open('app/newdata1.json')
        data = json.load(f)
        datas = data['resumes'][0]['data']
        name = datas['name']['raw']
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
        skillcount = 0
        locationcount=0
        educationcount=0
        experionscount = 0

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





            #company 
            companyskillcount = len(companyskill1)
            companyeducationcount = len(companyeducation)
            companyexperionscount= int(companyexperions)
            

            # Candidate
            candidateskillcount = skillcount
            candidateeducationcount = educationcount
            candidateexperionscount= int(experionscount)
            # print(candidateskillcount,candidateeducationcount,candidateexperionscount)
            


            Result = ((((candidateskillcount/companyskillcount)+(candidateeducationcount/companyeducationcount)+(candidateexperionscount/companyexperionscount))/3)*100)
            Result="{:.1f}".format(Result)
         
        





        # print((((4/7)+1+(5/10)+(2/2))/4)*100)   

        

            print("------------------------------The--Datas----------------------------------------------------")
            print(Candidateserilizer.data[i]['firstname'])
            print('education count',educationcount)
            print('skill count',skillcount)
            print('experions count',experionscount)

            print()
            print("percentage  :",Result,"%")
            print()
            
            # Matchdata.objects.create(name = name,skills=skillcount,education=educationcount)
            skillcount = 0
            educationcount = 0
            experionscount = 0





        return Response(Candidateserilizer.data,status=status.HTTP_200_OK)
        








        # companyjobtitle = Companyserilizer.data[0]['job_Title']
        # companylocations = ast.literal_eval(Companyserilizer.data[0]['locations']

                # print(companyskill)    #company skills in heres [k]---------------------------------
                # print(len(companyskill),"pppppp")
        # for i in range(0,len(Candidateserilizer.data)): 
        # companyjobtitle = Companyserilizer.data[0]['job_Title']
        # companylocations = ast.literal_eval(Companyserilizer.data[0]['locations']
            
        #     # print(len(Candidateserilizer.data))
        #     # for k in range(0,len(companyskill)):
        #     #     # print(companyskill)    #company skills in heres [k]---------------------------------
        #     #     # print(len(companyskill),"pppppp")
        #     #     datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
        #     #     for l in range(0,len(datas)):
        #     #         # print(datas[l])    #candidate skills in here [l] ---------------------------------------
        #     #         value = datas[l]
        #     #         if companyskill[k].lower() == value[0:len(companyskill[k])].lower():              #j[0:len(companyskill[i])].lower():
        #     #             skillcount=skillcount+1
            
        #     # # for k in range(0,len(companyeducation)):
                
        #     # #     # print(companyskill)    #company skills in heres [k]---------------------------------
        #     # #     # print(len(companyskill),"pppppp")
        #     # #     datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
        #     # #     for l in range(0,len(datas)):
        #     # #         # print(datas[l])    #candidate skills in here [l] ---------------------------------------
        #     # #         value = datas[l]
                    
        #     # #         if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
        #     # #             educationcount = educationcount +1
        #     # #             # print("educatiion")

       
        #     print("User name :",Candidateserilizer.data[i]['firstname'])
        #     print('skill count',skillcount)
        #     name = Candidateserilizer.data[i]['firstname']
        #     print('education count',educationcount)
        #     Matchdata.objects.create(name = name,skills=skillcount,education=educationcount)
        #     skillcount = 0
        #     educationcount = 0
        #     print("-----------------")
        




     

    

    

                
    #             class Checkdatas(APIView):

    # def get(self,request):
        
    #     skillcount = 0
    #     locationcount=0
    #     educationcount=0
    #     Company = JobType.objects.all()
    #     Companyserilizer =dataserilaizer(Company,many=True)
    #     companyskill = ast.literal_eval(Companyserilizer.data[0]['skills'])
    #     companyjobtitle = ast.literal_eval(Companyserilizer.data[0]['job_Title'])
    #     companyeducation = ast.literal_eval(Companyserilizer.data[0]['education'])
    #     # companylocations = ast.literal_eval(Companyserilizer.data[0]['locations'])

    




    #     Candidates = Candidate.objects.all()
    #     Candidateserilizer =candidateserilaizer(Candidates,many=True)
      
    #     for i in range(0,len(Candidateserilizer.data)): 
            
    #         print(len(Candidateserilizer.data))
    #         for k in range(0,len(companyskill)):
    #             # print(companyskill)    #company skills in heres [k]---------------------------------
    #             # print(len(companyskill),"pppppp")
    #             datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
    #             for l in range(0,len(datas)):
    #                 # print(datas[l])    #candidate skills in here [l] ---------------------------------------
    #                 value = datas[l]
    #                 if companyskill[k].lower() == value[0:len(companyskill[k])].lower():              #j[0:len(companyskill[i])].lower():
    #                     skillcount=skillcount+1
            
    #         for k in range(0,len(companyeducation)):
                
    #             # print(companyskill)    #company skills in heres [k]---------------------------------
    #             # print(len(companyskill),"pppppp")
    #             datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
    #             for l in range(0,len(datas)):
    #                 # print(datas[l])    #candidate skills in here [l] ---------------------------------------
    #                 value = datas[l]
                    
    #                 if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
    #                     educationcount = educationcount +1
    #                     # print("educatiion")

       
    #         print("User name :",Candidateserilizer.data[i]['firstname'])
    #         print('skill count',skillcount)
    #         name = Candidateserilizer.data[i]['firstname']
    #         print('education count',educationcount)
    #         Matchdata.objects.create(job_Title=companyjobtitle,name = name,skills=skillcount,education=educationcount)
    #         skillcount = 0
    #         educationcount = 0
    #         print("-----------------")
                    

                

    #     return Response(Candidateserilizer.data,status=status.HTTP_200_OK)




 