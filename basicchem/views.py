from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('First and main page')

def categories(request, cat):
    return HttpResponse(f'articles by categories, <p>{cat}</p>')

def basechem(requast):
    return HttpResponse('tasks for basic chemistry')

def mainpage(request):
    return HttpResponse('this is a project of a main page')

def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')