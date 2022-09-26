from django.urls import path
from .import views
from .views import *


urlpatterns = [
    
    path('convert/',convert.as_view(),name='convert'),    #List candidate data with include percentage

]
