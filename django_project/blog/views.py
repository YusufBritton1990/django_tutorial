from django.shortcuts import render #This directs to <root>/templates
from django.views.generic import ListView, DetailView
from .models import Post #the dot means the file is in the current folder

#view.home ran from urls.py in blog folder.
# for the date filter, check out django documentation
# https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date

# NOTE: Currently being replaced with PostListView class to view post
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # context variable is accessing posts dictionary
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    """
    arg:
        ListView: inherted from django.
    input:
        model: This is accessing the post data

        template_name: This is directing the post data to the home page as its
        template

        context_object_name: this is setting the variable to be called "posts"
        this will loop over all the post information

        ordering: this will show the most recent post at the top of a page.
        Note: if you want to do newest to oldest, put minus sign
    output:
        Displays posts on blog site, showing the most recent first
    """
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    """
    arg:
        DetailView: inherted from django.
    input:
        model: This is accessing the post data

    output:
        Display individual post when clicked. This data is routed into
        template post_detail.html which is dynamically populating the post
    """
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
