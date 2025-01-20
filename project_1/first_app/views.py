from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("home page of first app")

def courses(request):
    return HttpResponse("courses page from first app")