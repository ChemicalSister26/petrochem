from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *
# Create your views here.

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Main page', 'url_name': 'home'},
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Tasks', 'url_name': 'tasks'}]


def index(request):
    posts = Basicchem.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts, 'menu': menu, 'title': 'Main Page', 'cats': cats, 'cat_selected': 0}
    return render(request, 'Basicchem/index.html', context=context)


def articles(request):
    return HttpResponse('articles by categories')

def tasks(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})

def show_post(request, post_id):
    return HttpResponse(f'showing page with id = {post_id}')

def show_category(request, cat_id):
    posts = Basicchem.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts, 'menu': menu, 'title': 'Main Page', 'cats': cats, 'cat_selected': 0}
    return render(request, 'Basicchem/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')