from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page
from .views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'basicchem', BasicchemViewset)



urlpatterns = [
    path('', cache_page(60*15)(Basicchemmain.as_view()), name='home'),
    path('articles/', articles, name='articles'),
    path('tasks/', tasks, name='tasks'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BasicchemCats.as_view(), name='category'),
    path('add_feedback/', AddFeedbacks.as_view(), name='add_feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('api/v1/basicchemlist/', BasicchemAPIList.as_view()),
    path('api/v1/basicchemlist/<int:pk>/', BasicchemAPIUpdate.as_view()),
    path('api/v1/basicchemdelete/<int:pk>/', BasicchemAPIDestroy.as_view()),
    path('api/v1/auth_session/', include('rest_framework.urls')),
    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/basicchem/
]