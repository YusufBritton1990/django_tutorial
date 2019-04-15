from django.urls import path
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )
from . import views #. is for the current directory

"""
urlpatterns
after being called from django_project blog.urls, it will come to this folder
and run a path with an empty string. when it runs it, it will invoke
views.home

NOTE: views.home replaced with PostDetailView.as_view, which is showing
Post

blog-home: using PostDetailView class, this page contains the post

post-detail: based on the clicked post. it will only show information
on that individual post
    # NOTE: Once clicked, any reference in the template page itself will
    be referenced as "object". Also, the path to the template is
    <app>/<model>_<viewtype>.html, example: blog/post/1/.html

post-create: Generate a new field
    convention: <app>/<model>_<form>.html, example: blog/post/1/.html

post-update: update a post
    It will use the post template to update the post.
    convention: <app>/<model>_<form>.html, example: blog/post/1/update.html

post-delete: delete a post
    It will use the post_confirm_delete template to update the post.
    convention: <app>/<model>_<form>.html, example: blog/post/1/update.html

blog-about: routes to about page using views.about function
"""
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

"""

Reason for error when using PostListView.as_view() looking for a view by:

<app>/<model>_<viewtype>.html
"""
