from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def siva(request):
    return HttpResponse('siva is a good player')