from django.urls import path 
from . import views



urlpatterns = [   
    path('',views.climate,name='climate'),   
    
]