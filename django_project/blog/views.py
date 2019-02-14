from django.shortcuts import render #This directs to <root>/templates
from .models import Post #the dot means the file is in the current folder

#view.home ran from urls.py in blog folder.
# for the date filter, check out django documentation
# https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # context variable is accessing posts dictionary
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
