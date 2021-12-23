from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

menu = ['About us', 'Main page', 'Articles', 'Tasks']
def index(request):
    return render(request, 'Basicchem/index.html', {'menu': menu, 'title': 'Main Page'})

def categories(request, cat):
    return HttpResponse(f'articles by categories, <p>{cat}</p>')

def basechem(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')