from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employeedetails
import datetime


def plan(request):
    return HttpResponse('<h1>My First Plan</h1>')


def currentplan(request):
    dt = datetime.datetime.now()
    s = "<b>Current Plan time </b"+str(dt)
    return HttpResponse(dt)
# Create your views here.

def renderTemplate(request):
    mydict={"name":"Adarsh","age":23}
    return render(request,'templatesapp/firstTemplate.html',context=mydict)


def employeedata(request):
    employees=Employeedetails.objects.all()
    empdict={"employees":employees}
    return render(request,'templatesapp/index.html',context=empdict)