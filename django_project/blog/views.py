from django.shortcuts import render #This directs to <root>/templates
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
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

        paginate_by: Will display this amount of post on a page at a time
            Note: using this input, is_paginated exist amd can use
            page_obj in templates
    output:
        Displays posts on blog site, showing the most recent first
    """
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 3

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

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    arg:
        LoginRequiredMixin: This will require a user to be logged in to be able to make a post. If a user isn't logged it, the page will redirect to login page
        CreateView: inherted from django.
    input:
        model: This is accessing the post data
        fields: fields that user will complete for post

        form_valid(): This is used to overide the author, which is currently blank
    output:
        Generate a new post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        args:
            self: This will add to class
            form: This is altering the form

        input:
            form.instance.author: The instance the form is created, it will make author equal the author, which is passed in with the HTTP Post request (current logged in user)

        output:
            this will override the form_valid() that is in super, which will now have the author set to the current logged in user

        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    arg:
        LoginRequiredMixin: This will require a user to be logged in to be able to make a post. If a user isn't logged it, the page will redirect to login page
        UserPassesTestMixin: This will allow only the logged in user to edit their post.
        CreateView: inherted from django.
    input:
        model: This is accessing the post data
        fields: fields that user will complete for post

        form_valid(): This is used to overide the author, which is currently blank
    output:
        Generate a new post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        args:
            self: This will add to class
            form: This is altering the form

        input:
            form.instance.author: The instance the form is created, it will make author equal the author, which is passed in with the HTTP Post request (current logged in user)

        output:
            this will override the form_valid() that is in super, which will now have the author set to the current logged in user

        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        input:
            get_object(): This is selecting the post we are updating

        output:
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    arg:
        LoginRequiredMixin: This will require a user to be logged in to be able to make a post. If a user isn't logged it, the page will redirect to login page
        UserPassesTestMixin: This will allow only the logged in user to edit their post.
        DetailView: inherted from django.
    input:
        model: This is accessing the post data
        success_url: Once post is deleted, it will redirect to the homepage
        (it's name is '/' or '', as defined in urls.py)

    output:
        Display individual post when clicked. This data is routed into
        template post_detail.html which is dynamically populating the post
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        input:
            get_object(): This is selecting the post we are updating

        output:
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
