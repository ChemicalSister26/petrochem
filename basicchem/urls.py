from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('articles/<slug:cat>/', categories),
    path('tasks/', basechem),
]