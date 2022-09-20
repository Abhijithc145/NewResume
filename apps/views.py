from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json    
import re 
from .models import *
from .serializer import *
import ast


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
        # sudo -u postgres psql
        
        f = open('apps/data1.json')
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
            if datas['location']['formatted'].exits():
                address=datas['location']['formatted']
                location=datas['location']['state']
                
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
        
            Candidate_data.objects.create(firstname=name,address=address,skills=skills,education=[*set(education)],personemails=personemails[0],phonenumber=phonenumber,language=language,experions=experience,websites=websites,location=location)
            return Response(datas,status=status.HTTP_200_OK)
        except:
            return Response(data,status=status.HTTP_204_NO_CONTENT)
            
 
        
class Addjobs(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = JobType_json1.objects.all()
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
        Company = JobType_data.objects.all()
        Companyserilizer =dataserilaizer(Company,many=True)
        companyskill = ast.literal_eval(Companyserilizer.data[0]['skills'])
        companyeducation = ast.literal_eval(Companyserilizer.data[0]['education'])
        companylocations = ast.literal_eval(Companyserilizer.data[0]['locations'])

    




        Candidates = Candidate_data.objects.all()
        Candidateserilizer =candidateserilaizer(Candidates,many=True)
      
        # for i in range(0,len(Candidateserilizer.data)):
            
        #     # print(len(Candidateserilizer.data))
        #     for k in range(0,len(companyskill)):
        #         # print(companyskill)    #company skills in heres [k]---------------------------------
        #         # print(len(companyskill),"pppppp")
        #         datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
        #         for l in range(0,len(datas)):
        #             # print(datas[l])    #candidate skills in here [l] ---------------------------------------
        #             value = datas[l]
        #             if companyskill[k].lower() == value[0:len(companyskill[k])].lower():              #j[0:len(companyskill[i])].lower():
        #                 skillcount=skillcount+1
            
        #     for k in range(0,len(companyeducation)):
        #         # print(companyskill)    #company skills in heres [k]---------------------------------
        #         # print(len(companyskill),"pppppp")
        #         datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
        #         for l in range(0,len(datas)):
        #             # print(datas[l])    #candidate skills in here [l] ---------------------------------------
        #             value = datas[l]
                    
        #             if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
        #                 educationcount = educationcount +1
        #                 print("educatiion")


            # Candidate.objects.create()
            # print(Candidateserilizer.data[i]['firstname'])
            # print('skill count',skillcount)
            # print('education count',educationcount)
            # skillcount = 0
            # educationcount = 0
            # print("-----------------")
                    

                

        for j in range(0,3):
            pass    
         

                    



                    


                  
            
            
        return Response(Candidateserilizer.data,status=status.HTTP_200_OK)
    













            # skills = ast.literal_eval(Candidateserilizer.data[q]['skills'])
    
#  print(len(skills))
#             #
#             for i in range(0,len(skills)):
#                 print(skills[i])
#                 skillscount=skillscount+1   
#             print(skillscount)   
                
                
                # print("=========================3====================")
                # # print(Candidateserilizer.data[w]['skills']
                # print(ast.literal_eval(Companyserilizer.data----")
                # print(ast.literal_eval(Candidateserilizer.data[w]['skills']),"--------3-")






        # Checkskill =ast.literal_eval(Candidateserilizer.data[0]['skills'])
        # for i in range(0,len(Candidateserilizer.data)):
        #     print()

        # skills=ast.literal_eval(Candidateserilizer.data[0]['skills'])
        # for i in skills:
        #     print(i)
        # print('-----1-------------------------')
        # for q in range(0,len(Companyserilizer.data)):
        #     for w in range(0,len(Candidateserilizer.data)):
        #         for e in range(0,len(Companyserilizer.data[q]['skills'])):
        #             print("hhhh")
                    # print(ast.literal_eval(Companyserilizer.data[e]['skills'][w]),"jjjjjjjjjjjjjjjjjjjjjjjjjjj")
                    # for r in range(0,len(Candidateserilizer.data[w]['skills'])):
                    #     print(ast.literal_eval(Candidateserilizer.data[r]['skills'][w]),"llllllllllllllllllllllllllllllllll")

  # for i in range(0,len(Candidateserilizer.data)):
        #     print(len(Candidateserilizer.data))

        #     # for k in range(0,len(companyskill)):
        #     for j in ast.literal_eval(Candidateserilizer.data[i]['skills']):
        #         if companyskill[i] == j[0:len(companyskill[i])].lower():
        #             skillcount = skillcount+1
                    
        #         else:
        #             print("",end="") 
        #             # print(j[0:3].lower()) 

        #     for k in range(0,len(companyeducation)):
        #         for j in ast.literal_eval(Candidateserilizer.data[i]['education']):
        #             if companyskill[k] == j[0:len(companyeducation[k])].lower():
        #                 educationcount = educationcount+1
                        
        #             else:
        #                 print("",end="") 
        #                 # print(j[0:3].lower())  
        #                 #            
        #     print("-----------------Match Datas------------")
        #     print("Skills =",skillcount) 
        #     print("Education=",educationcount)   




           # for j in range(0,len(companyskill)):
            #     print("skills")
            #     print(len(companyskill))
            
        # print(companylocations,"oooooooooooooooooooooooooooooooooooooooooooo")
        # for i in companylocations:
        #     print(i)
