from django.urls import path
from .views import PostListView, PostDetailView
from . import views #. is for the current directory

"""
urlpatterns
after being called from django_project blog.urls, it will come to this folder
and run a path with an empty string. when it runs it, it will invoke
views.home

NOTE: views.home replaced with PostDetailView.as_view, which is showing
Post

blog-home: using PostDetailView class, this page contains the post
post-detail: based on information
blog-about: routes to about page using views.about function
"""
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]

"""

Reason for error when using PostListView.as_view() looking for a view by:

<app>/<model>_<viewtype>.html
"""
