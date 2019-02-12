from django.urls import path
from . import views #. is for the current directory

#after being called from django_project blog.urls, it will come to this folder
#and run a path with an empty string. when it runs it, it will invoke
#views.home
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
