from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def hora(request):
    dt=datetime.datetime.now()
    s="<h1>Fecha y hora actuales en Chile UCT-8</h1>"+str(dt)
    return HttpResponse(s)
    
def pagina(request):
    return HttpResponse("<h1> Pagina nueva </h1>") 

def pagina2(request):
    return HttpResponse("<h2> Pagina nueva </h2>") 

def pagina3(request):
    return HttpResponse("<h3> Pagina nueva </h3>")    
