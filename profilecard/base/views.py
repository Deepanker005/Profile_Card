from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("The is a new page")

# Create your views here.
