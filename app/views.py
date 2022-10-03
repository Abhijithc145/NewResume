import stat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
import ast,json,re 
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
import PyPDF2
from django.db.models import Q

# Create your views here.


class Datas(APIView):
    def get(self,request):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        skills=[]
        language=[]
        education =[]
        websites = []
        secondemails =0
        f = open('app/Resume/R10.json')
        data = json.load(f)
        try:
            datas = data['resumes'][0]['data']
        except:
            # return Response({'Error':'The Key and Values  are not formated in the json '},status=status.HTTP_404_NOT_FOUND)
            return Response(data,status=status.HTTP_404_NOT_FOUND)
        try:    
            name = datas['name']['raw']
        except:
            name ='Name is not available'    
        try:
            location = datas['location']['state']
        except:
            location = "No location"
        tttt =0
        personemails=0
        if datas['emails']==[]:
            try:
                for i in range(0,len(datas['sections'])):
                    # print(len(datas['sections'][i]))
                    if secondemails == 0 or secondemails == []:
                        
                        if datas['sections'][i]['sectionType'] == "PersonalDetails":
                            tttt=datas['sections'][i]['text']
                            secondemails= re.findall( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', tttt)
                            if secondemails != 0 or secondemails != []:
                                personemails = secondemails
                            else:    
                                print("-------------1-------------")     
                        else:
                            print(datas['emails'].exists())
                    else:
                        print("-----------------------3-----------------------")
                        break
            except:
                print("--------------------4----------------------")
                if datas['emails'] == [] and datas['phoneNumbers'] ==[]:
                    return Response({'Error':'Email and phone number is not available in this json data,  Please enter the another resume'},status=status.HTTP_204_NO_CONTENT) 
        else :
            print("----------------------5----------------------")
            personemails = datas['emails']
 
        try:
            experience= datas['totalYearsExperience']

        except:
            experience=0
        try:
            phonenumber = datas['phoneNumbers'][0]

        except:
            phonenumber="No phone number"

        try:
            address=datas['location']['formatted']
        except:
            address="No address"

        
        for i in range(0,len(datas['websites'])):
            websites.append(datas['websites'][i])
        
        
        for i in range(0,len(datas['education'])):
            education.append(datas['education'][i]['accreditation']['inputStr'])
        

        for i in range(0,len(datas['languages'])):
            language.append(datas['languages'][i])    

        for i in range(0,len(datas['skills'])):
            skills.append(datas['skills'][i]['name']) 



        print(personemails)
        print(type(personemails),";;;;;;;;;;;;;;;;;;;;;;;;;;;;")  
        # personemails = personemails.split(",")
        for i in range(0,len(personemails)):
            secondemails= re.findall( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',personemails[i])
            print(secondemails,"oooooooooooooooooooooowwwwwwwwwwwwwoooooooooooooooooooo")
            # if secondemails != 0 or secondemails != []:
            #     personemails = secondemails
            # else:    
            #     print("-------------1-------------")  

        try:      
            # Candidate.objects.create(firstname=name,address=address,skills=skills,education=education,locations=location,personemails=personemails[0],phonenumber=phonenumber,language=language,experions=experience,websites=websites)
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({'Error':'The Email address or Phone number is already added in  another resumes .....! ,please Check..it......'})
        # return Response(data,status=status.HTTP_200_OK)
 
        
class Addjobs(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = JobType.objects.all()
    serializer_class = dataserilaizer
    # permission_classes = False

    def get(self,request,*args,**kwargs):

        return self.list(request,*args,**kwargs)   

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)  


class Addjobss(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = JobType.objects.all()
    serializer_class = dataserilaizer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)  

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class Addjobss(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = JobType.objects.all()
    serializer_class = dataserilaizer


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)  

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)    
















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

        skillsare=[]
        locationsare=[]
        educationsare=[]
        experionsare=0
        emailare = 0
        dataaddedvalues = []

        average = 0
        Company = JobType.objects.all()
        Companyserilizer =dataserilaizer(Company,many=True)

        

        
        # print(len(Company))
        for v in range(0,len(Company)):
            print(Companyserilizer.data[v],"company .....d")



            job_type =  Companyserilizer.data[v]['job_Type']
            print(job_type,"--------------------Job Type--------------------")

            companyskill = Companyserilizer.data[v]['skills']
    
            companyeducation1 = Companyserilizer.data[v]['education']
            companyexperions = Companyserilizer.data[v]['experions']
            companylocation=Companyserilizer.data[v]['locations'].split(",")
            
            try:
                companylocationcount=len(Companyserilizer.data[v]['locations'])
            except:
                pass

            companyexperions=companyexperions[0]

            companyskill1 = companyskill.split(",")
            companyeducation=companyeducation1.split(",")

            Candidates = Candidate.objects.all()
            Candidateserilizer =candidateserilaizer(Candidates,many=True)

            for i in range(0,len(Candidateserilizer.data)): 
                emailare=Candidateserilizer.data[i]['personemails']

                # experionsare=
                # if 
                

                for k in range(0,len(companyskill1)):
                    datas=ast.literal_eval(Candidateserilizer.data[i]['skills'])
                    for l in range(0,len(datas)):
                        value = datas[l]
                        if companyskill1[k].lower() == value[0:len(companyskill1[k])].lower():             
                            skillcount=skillcount+1
                            skillsare.append(value[0:len(companyskill1[k])].upper())
            

                for k in range(0,len(companyeducation)):
                    datas=ast.literal_eval(Candidateserilizer.data[i]['education'])
                    for l in range(0,len(datas)):
                        value = datas[l]    
                        if companyeducation[k].lower() == value[0:len(companyeducation[k])].lower(): 
                            educationcount = educationcount +1
                            educationsare.append(value[0:len(companyeducation[k])].upper())

                if int(Candidateserilizer.data[i]['experions']) >= int(companyexperions):

                    experionscount =  companyexperions
            
                else:
                
                    experionscount =  Candidateserilizer.data[i]['experions']
                        

                datas=Candidateserilizer.data[i]['locations']
                for p in datas:
                    dataaddedvalues.append(p)
                
                for k in range(0,len(companylocation)):

                    if companylocation[k].lower() == datas.lower():
                        locationcount=locationcount+1
                        locationTrue = "yes"
                        locationsare.append(datas)

                    else:
                        if locationcount == 0:
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
            
                Result = ((((candidateskillcount/companyskillcount)+(locationcount/1)+(candidateeducationcount/companyeducationcount)+(candidateexperionscount/companyexperionscount))/4)*100)
                Result="{:.1f}".format(Result)
    
                Candidatename = Candidateserilizer.data[i]['firstname']
                # print(candidateexperionscount,"          ",companyexperionscount)
                # print(candidateskillcount,"              ",companyskillcount)
                # print(locationcount,"       ",1)
                # print(candidateeducationcount,"        ",companyeducationcount)
                # # (candidateexperionscount/companyexperionscount)
                # print("                             The--Datas                                  ")
                # print("")
                # print("           Name   ",Candidatename)
                # print('')
                # print('              education count',educationcount,"The educations are",educationsare) 
                # print('              skill count',skillcount," the skills are ",skillsare)
                # print('              experions count',experionscount ,"       ",experionsare)
                # print('              Location',locationTrue,'The locations are',locationsare)
                # print()
                # print("              percentage  :",Result,"%")
                # print(emailare)
                
                if Matchdata.objects.filter(emails=emailare ,job_Type=job_type).exists():
                    print("data")
                else:
                    Matchdata.objects.create(job_Type=job_type,name = Candidatename,emails=emailare,skills=skillsare,locations=locationsare,education=educationsare,experions=experionscount,percentage=Result)
                    
                skillsare=[]
                educationsare=[]
                locationsare=[]
                emailare=0
                companyexperionscount=0

                skillcount = 0
                educationcount = 0
                locationcount=0
                experionscount = 0


        return Response(Candidateserilizer.data,status=status.HTTP_200_OK)






class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        datas = Matchdata.objects.all().order_by('-percentage').values()
        serializers = Matchserilaizer(datas,many = True)
        return Response(serializers.data,status=status.HTTP_200_OK)


class Checkdata_list(APIView):
    def get(self,request,pk):
        
        try:
            data = JobType.objects.get(id = pk)
            data_serilizer = dataserilaizer(data).data

            values = data_serilizer['job_Type']

            filter_data = Matchdata.objects.all()
            filter_serilizer = Matchserilaizer(filter_data,many=True).data

            if Matchdata.objects.filter(job_Type=values):
                datass =Matchserilaizer(Matchdata.objects.filter(job_Type=values).order_by('-percentage').values(),many=True).data
                return Response(datass,status=status.HTTP_200_OK)
                
            else:
                return Response({'Error':"No Datas are available in the Table"},status=status.HTTP_200_OK)
        except:
            return Response({'Error':"No Datas are available in the Table"},status=status.HTTP_200_OK)

 


class Listdatas(APIView):
    def get(self,request):
        pdf_file = open('app/all.pdf', 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # page_content
        data = json.dumps(page_content)
        formatj = json.loads(data)
        return Response(page_content,status=status.HTTP_200_OK)

    
class JobaddPdf(APIView):
    def get(self,request):
        Educationsl_datas =['MTech','BTech','BE','MCA','BCA','Bcom','BA','IT',]
        skills=[]
        language=[]
        f = open('app/Companyjd.json')
        data = json.load(f)
        datas = data['resumes'][0]['data']
        All=datas
        for i in range(0,len(datas['skills'])):
            skills.append(datas['skills'][i]['name']) 
        for i in range(0,len(datas['languages'])):
            language.append(datas['languages'][i])    
        totalYearsExperience = datas['totalYearsExperience']   
        print("------------------------------------------------------")
        print(skills)
        print(language)
        print(totalYearsExperience)
        return Response(data,status=status.HTTP_200_OK)   
                  

                  