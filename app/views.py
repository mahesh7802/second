from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def lover(request):
    return HttpResponse('<marquee><h1>girl: hii ra pichoda how are you</marpuee></h1><h1>boy: hii ra</h1>')


 
