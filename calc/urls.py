#import path 
from django.urls import path

#import views
from . import views

urlpatterns =  [
    #for homepage url is either blank(' ') or slash ('/')
    #for this home function to work we need to define it in the views program first
    #then we also need to add this path in the main urls.py of the project 
    path('', views.home, name = 'home'),
    path('add', views.add, name = 'add')
]