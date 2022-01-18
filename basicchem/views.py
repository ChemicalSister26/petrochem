from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import *
# Create your views here.

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Main page', 'url_name': 'home'},
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Tasks', 'url_name': 'tasks'},
        {'title': 'Add feedback', 'url_name': 'add_feedback'}]


def index(request):
    post = Basicchem.objects.all()
    cats = Category.objects.all()
    context = {'post': post,
               'menu': menu,
               'title': 'Main Page',
               'cats': cats,
               'cat_selected': 1}
    return render(request, 'Basicchem/index.html', context=context)


def articles(request):
    return HttpResponse('articles by categories')

def tasks(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})

def show_post(request, post_slug):
    post = get_object_or_404(Basicchem, slug=post_slug)
    cats = Category.objects.all()

    context = {'post': post,
               'menu': menu,
               'title': post.title,
               'cats': cats,
               'cat_selected': post.cat_id}

    return render(request, 'Basicchem/post.html', context=context)

def show_category(request, cat_slug):
    cats = Category.objects.filter(slug=cat_slug)
    post = Basicchem.objects.filter(cat_id=cats[0].id)


    if len(post) == 0:
        raise Http404()

    context = {'post': post,
               'menu': menu,
               'title': 'Main Page',
               'cats': cats,
               'cat_selected': cats[0].id}
    return render(request, 'Basicchem/category.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')

def add_feedback(request):
    if request.method == 'POST':
        form = Addfeedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Addfeedback()
    return render(request, 'Basicchem/addfeedback.html', {'form': form, 'menu': menu, 'title': 'Add Feedback'})