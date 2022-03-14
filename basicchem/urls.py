from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', Basicchemmain.as_view(), name='home'),
    path('articles/', articles, name='articles'),
    path('tasks/', tasks, name='tasks'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BasicchemCats.as_view(), name='category'),
    path('add_feedback/', AddFeedbacks.as_view(), name='add_feedback'),
    path('login/', login, name='login'),
    path('registration/', RegisterUser.as_view(), name = 'registration')

]