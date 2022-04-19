from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'basicchem', BasicchemViewset)

urlpatterns = [
    path('', Basicchemmain.as_view(), name='home'),
    path('articles/', articles, name='articles'),
    path('tasks/', tasks, name='tasks'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BasicchemCats.as_view(), name='category'),
    path('add_feedback/', AddFeedbacks.as_view(), name='add_feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    # path('api/v1/basicchemlist', BasicchemViewset.as_view({'get': 'list'})),
    # path('api/v1/basicchemlist/<int:pk>/', BasicchemViewset.as_view({'put': 'update'})),
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/basicchem/
]