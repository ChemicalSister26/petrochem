from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('articles/<slug:cat>/', categories),
    path('tasks/', basechem),
    path('about/', about, name='about'),
]