from django.urls import path
from .import views
from .views import *


urlpatterns = [
     path('addjobs/',Addjobs.as_view(),name='addjobs'),        #Add job in company
     path('addjobs/<int:pk>',Addjobss.as_view(),name='addjobs'),        #Add job in company
     path('data/',Datas.as_view(),name='details'),             #Json data add in models
     path('checkdata/',Checkdata.as_view(),name='checkdata'),  #Check company data and candidate data 
     path('jobpdf/',JobaddPdf.as_view(),name='jobpdf'),    #List candidate data with include percentage

]
