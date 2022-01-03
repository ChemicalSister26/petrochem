from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('articles/', articles, name='articles'),
    path('tasks/', tasks, name='tasks'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    path('add_feedback/', add_feedback, name='add_feedback')
]