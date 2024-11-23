from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def peddakka(request):
    return HttpResponse('<h1> <marquee> name is peddakka  </marquee> </h1>')