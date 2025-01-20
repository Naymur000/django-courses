from django.shortcuts import render
from django.http import HttpResponse

def home(ruquest):
    return HttpResponse("home page of second app")

def courses(request):
    return HttpResponse("courses page from second app")

