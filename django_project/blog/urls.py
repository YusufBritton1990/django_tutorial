from django.urls import path
from .views import PostListView
from . import views #. is for the current directory

#after being called from django_project blog.urls, it will come to this folder
#and run a path with an empty string. when it runs it, it will invoke
#views.home
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

"""

Reason for error when using PostListView.as_view() looking for a view by:

<app>/<model>_<viewtype>.html
"""
