#import path 
from django.urls import path

#import views
from . import views

urlpatterns =  [
    path('', views.index, name = 'index')
]