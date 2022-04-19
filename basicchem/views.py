from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from rest_framework import generics
from rest_framework.response import Response

from .serializer import BasicchemSerializer
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

def logout_user(request):
    logout(request)
    return redirect('login')


def articles(request):
    return HttpResponse('articles by categories')

def tasks(requast):
    return HttpResponse('tasks for basic chemistry')

def about(request):
    return render(request, 'Basicchem/about.html', {'menu': menu, 'title': 'About us'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Basicchem/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



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



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Basicchem/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

class BasicchemAPIView(generics.ListAPIView):
    queryset = Basicchem.objects.all()
    serializer_class = BasicchemSerializer
    
class BasicchemAPIUpdate(generics.UpdateAPIView):
    queryset = Basicchem.objects.all()
    serializer_class = BasicchemSerializer

class BasicchemAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basicchem.objects.all()
    serializer_class = BasicchemSerializer

    





