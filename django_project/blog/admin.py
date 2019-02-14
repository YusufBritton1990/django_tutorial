from django.contrib import admin
from .models import Post

# adds posts to admin page
admin.site.register(Post)
