from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kumari(request):
    return HttpResponse('<h1> kumari is a innocent girl </h1>')