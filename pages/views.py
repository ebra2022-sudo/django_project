from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# first import the
def homePageView(request):
    return HttpResponse("Hello, World!")
