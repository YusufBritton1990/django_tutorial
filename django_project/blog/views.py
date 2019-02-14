from django.shortcuts import render #This directs to <root>/templates
from .models import Post #the dot means the file is in the current folder

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]



#view.home ran from urls.py in blog folder.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # context variable is accessing posts dictionary
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
