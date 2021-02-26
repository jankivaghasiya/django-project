from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

#creating the home function 
#if we are getting data in request format we need to send it back in the response format 
#def home(request) :
#    return HttpResponse("Hey! I am Janki...... wohoooooooooooo........ hehehehehe")


#for including html page
#using dictionary to make variable dynamic
def home(request) :
    return render(request, 'home.html', {'name' : 'Jaankeeyyy :)'})

def add(request) :
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result' : res})