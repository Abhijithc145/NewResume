from django.urls import path
from .import views
from .views import *


urlpatterns = [
     
     path('alldatacheck/',allDataCheck.as_view(),name='alldatacheck'),    #List candidate data with include percentage

]
