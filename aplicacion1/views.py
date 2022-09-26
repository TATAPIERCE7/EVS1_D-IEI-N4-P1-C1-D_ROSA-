from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def texto(request):
    return HttpResponse("<h1> Texto Prueba </h1>")

