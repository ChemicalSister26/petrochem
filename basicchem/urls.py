from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', Basicchemmain.as_view(), name='home'),
    path('articles/', articles, name='articles'),
    path('tasks/', tasks, name='tasks'),
    path('about/', about, name='about'),
    path(r'post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path(r'category/<slug:cat_slug>/', BasicchemCats.as_view(), name='category'),
    path(r'add_feedback/', AddFeedbacks.as_view(), name='add_feedback'),
    path(r'login/', LoginUser.as_view(), name='login'),
    path(r'logout/', logout_user, name='logout'),
    path(r'registration/', RegisterUser.as_view(), name='registration'),
    path(r'api/v1/basicchemlist', BasicchemAPIList.as_view()),
    path(r'api/v1/basicchemlist/<int:pk>/', BasicchemAPIList.as_view()),
]
