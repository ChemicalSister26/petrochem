
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import *
from .models import *
# Create your views here.

from .utils import *

menu = [{'title': 'About us', 'url_name': 'about'},
        {'title': 'Main page', 'url_name': 'home'},
        {'title': 'Articles', 'url_name': 'articles'},
        {'title': 'Tasks', 'url_name': 'tasks'},
        {'title': 'Add feedback', 'url_name': 'add_feedback'}]

cats = Category.objects.all()

class Basicchemmain(DataMixin, ListView):
    model = Basicchem
    template_name = 'Basicchem/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cats'] = cats
        return context



def articles(request):
    return HttpResponse('articles by categories')

def tasks(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})






class ShowPost(DataMixin, DetailView):
    model = Basicchem
    template_name = 'Basicchem/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        context['cats'] = cats

        return context



class BasicchemCats(DataMixin, ListView):
    model = Basicchem
    template_name = 'Basicchem/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['post'][0].cat)
        context['cat_selected'] = context['post'][0].cat_id
        context['cats'] = cats
        return context

    def get_queryset(self):
        return Basicchem.objects.filter(cat__slug=self.kwargs['cat_slug'])




def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')




class AddFeedbacks(LoginRequiredMixin, CreateView):
    form_class = Addfeedback
    template_name = 'Basicchem/add_feedback.html'
    login_url = '/admin/'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add feedback'
        return context

# def add_feedback(request):
#     if request.method == 'POST':
#         form = Addfeedback(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = Addfeedback()
#
#     return render(request, 'Basicchem/addfeedback.html', {'form': form, 'menu': menu, 'title': 'Add Feedback'})