from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bioData(request):
    return HttpResponse('<h1> hari 23 male </h1>')