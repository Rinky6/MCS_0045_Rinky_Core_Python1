from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello Rinky")


def index1(request):
    response=""" <h1> My first project </h2>"""
    return HttpResponse(response)
s