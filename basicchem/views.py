from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('First and main page')

def categories(request):
    return HttpResponse('articles by categories')

def basechem(requast):
    return HttpResponse('tasks for basic chemistry')

def mainpage(request):
    return HttpResponse('this is a project of a main page')