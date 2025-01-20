from django.http import HttpResponse

def home(request):
    return HttpResponse("home page of project 1")

def contact(request):
    return HttpResponse("conract page")