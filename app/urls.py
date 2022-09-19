from django.urls import path
from .import views
from .views import *


urlpatterns = [
     path('data/',Datas.as_view(),name='details'),

]
