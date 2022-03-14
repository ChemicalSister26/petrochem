
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .utils import *
from .forms import *
from .models import *
# Create your views here.

from .utils import *



cats = Category.objects.all()

class Basicchemmain(DataMixin, ListView):

    model = Basicchem
    template_name = 'Basicchem/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(c_def.items()))



def articles(request):
    return HttpResponse('articles by categories')

def tasks(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})

def login(request):
    return render(request, 'Basicchem/login.html')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Basicchem/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))



class ShowPost(DataMixin, DetailView):
    model = Basicchem
    template_name = 'Basicchem/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))



class BasicchemCats(DataMixin, ListView):

    model = Basicchem
    template_name = 'Basicchem/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['post'][0].cat), cat_selected = context['post'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Basicchem.objects.filter(cat__slug=self.kwargs['cat_slug'])




def pageNotFound(request, exception):
    return HttpResponseNotFound('unfortunately page not found')




class AddFeedbacks(LoginRequiredMixin, DataMixin, CreateView):
    form_class = Addfeedback
    template_name = 'Basicchem/add_feedback.html'
    login_url = reverse_lazy('home')
    #raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add Feedback')
        return dict(list(context.items()) + list(c_def.items()))

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