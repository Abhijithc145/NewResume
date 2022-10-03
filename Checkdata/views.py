from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
import ast,json,re 
from app.models import *
from app.serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
import PyPDF2
from django.db.models import Q


class allDataCheck(APIView):
    def get(self,request):
        Company = JobType.objects.all()
        Companyserilizer =dataserilaizer(Company,many=True).data

        Candidates =Candidate.objects.all()
        candidateserilaizers= candidateserilaizer(Candidates,many = True).data


        #Company Datas
        company_Skills_Count = 0
        company_Location_Count = 0
        company_Education_Count = 0
        company_Experionce_Count = 0


        educationsare=[]


        for i in range(0,len(Companyserilizer)):

            #Company datas are featch in the sutable varialbles

            company_Job_Types = Companyserilizer[i]['job_Type']
            company_Skills = Companyserilizer[i]['skills'].split(",")
            company_Locations = Companyserilizer[i]['locations'].split(',')
            company_Education = Companyserilizer[i]['education'].split(',')
            company_Experions=Companyserilizer[i]['experions']

            for j in range(0,len(candidateserilaizers)):
                candidate_Name = candidateserilaizers[j]['firstname']
                candidate_Experions = candidateserilaizers[j]['experions']
                candidate_Locations = candidateserilaizers[j]['locations']




                # print(len(candidateserilaizers[j]['education']))
                for k in range(0,len(company_Education)):
                    datas=ast.literal_eval(candidateserilaizers[j]['education'])
                    for l in range(0,len(datas)):
                        value = datas[l]    
                        if company_Education[k].lower() == value[0:len(company_Education[k])].lower(): 
                            print("lala")
                    print("-----------------------------")    
                        #     educationsare.append(value[0:len(company_Education[k])].upper())

                # print(educationsare)  
                educationsare=[]         
            


           



        return Response(candidateserilaizers,status=status.HTTP_200_OK)



        # skillcount = 0
        # locationcount=0
        # educationcount=0
        # experionscount = 0
        # locationcount =0

        # locationTrue = "No"
        # companyexperionscount = 0
        # companyeducationcount=0
        # companyskillcount = 0

        # skillsare=[]
        # locationsare=[]
        # educationsare=[]
        # experionsare=0
        # emailare = 0
        # dataaddedvalues = []

        # average = 0

        

        
        # # print(len(Company))
        # # for v in range(0,len(Company)):
        # #     print(Companyserilizer[v],"company .....d")



        # job_type =  Companyserilizer.data[0]['job_Type']
        # print(job_type,"--------------------Job Type--------------------")

        # companyskill = Companyserilizer.data[0]['skills']
   
        # companyeducation1 = Companyserilizer.data[0]['education']
        # companyexperions = Companyserilizer.data[0]['experions']
        # companylocation=Companyserilizer.data[0]['locations'].split(",")
        
        # try:
        #     companylocationcount=len(Companyserilizer.data[0]['locations'])
        # except:
        #     pass

        # companyexperions=companyexperions[0]

        # companyskill1 = companyskill.split(",")
        # companyeducation=companyeducation1.split(",")

        # Candidates = Candidate.objects.all()
        # Candidateserilizer =candidateserilaizer(Candidates,many=True)

        # for i in range(0,len(Candidateserilizer.data)): 
        #     emailare=Candidateserilizer.data[i]['personemails']

        #     # experionsare=
        #     # if 
            

        #     for k in range(0,len(companyskill1)):
        #         datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
        #         for l in range(0,len(datas)):
        #             value = datas[l]
        #             if companyskill1[k].lower() == value[0:len(companyskill1[k])].lower():             
        #                 skillcount=skillcount+1
        #                 skillsare.append(value[0:len(companyskill1[k])].upper())
           

        #     for k in range(0,len(companyeducation)):
        #         datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
        #         for l in range(0,len(datas)):
        #             value = datas[l]    
        #             if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
        #                 educationcount = educationcount +1
        #                 educationsare.append(value[0:len(companyeducation[k])].upper())

        #     if int(Candidateserilizer.data[i]['experions']) >= int(companyexperions):

        #         experionscount =  companyexperions
          
        #     else:
             
        #         experionscount =  Candidateserilizer.data[i]['experions']
                    

        #     datas=Candidateserilizer.data[i]['locations']
        #     for p in datas:
        #         dataaddedvalues.append(p)
               
        #     for k in range(0,len(companylocation)):

        #         if companylocation[k].lower() == datas.lower():
        #             locationcount=locationcount+1
        #             locationTrue = "yes"
        #             locationsare.append(datas)

        #         else:
        #             if locationcount == 0:
        #                 locationcount=0
        #                 locationTrue= 'NO'
        
        #     #company 
        #     companyskillcount = len(companyskill1)
        #     companyeducationcount = len(companyeducation)
        #     companyexperionscount= int(companyexperions)
            

        #     # Candidate
        #     candidateskillcount = skillcount
        #     candidateeducationcount = educationcount
        #     candidateexperionscount= int(experionscount)
          
        #     Result = ((((candidateskillcount/companyskillcount)+(locationcount/1)+(candidateeducationcount/companyeducationcount)+(candidateexperionscount/companyexperionscount))/4)*100)
        #     Result="{:.1f}".format(Result)
  
        #     Candidatename = Candidateserilizer.data[i]['firstname']
        #     # print(candidateexperionscount,"          ",companyexperionscount)
        #     # print(candidateskillcount,"              ",companyskillcount)
        #     # print(locationcount,"       ",1)
        #     # print(candidateeducationcount,"        ",companyeducationcount)
        #     # # (candidateexperionscount/companyexperionscount)
        #     # print("                             The--Datas                                  ")
        #     # print("")
        #     # print("           Name   ",Candidatename)
        #     # print('')
        #     # print('              education count',educationcount,"The educations are",educationsare) 
        #     # print('              skill count',skillcount," the skills are ",skillsare)
        #     # print('              experions count',experionscount ,"       ",experionsare)
        #     # print('              Location',locationTrue,'The locations are',locationsare)
        #     # print()
        #     # print("              percentage  :",Result,"%")
        #     # print(emailare)
            
        #     if Matchdata.objects.filter(emails=emailare ,job_Type=job_type).exists():
        #         print("data")
        #     else:
        #         Matchdata.objects.create(job_Type=job_type,name = Candidatename,emails=emailare,skills=skillsare,locations=locationsare,education=educationsare,experions=experionscount,percentage=Result)
                
        #     skillsare=[]
        #     educationsare=[]
        #     locationsare=[]
        #     emailare=0
        #     companyexperionscount=0

        #     skillcount = 0
        #     educationcount = 0
        #     locationcount=0
        #     experionscount = 0


        # return Response(Candidateserilizer.data,status=status.HTTP_200_OK)
