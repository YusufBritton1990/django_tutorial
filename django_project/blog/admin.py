from django.contrib import admin
from .models import Post #whenever you are making models, need to register here

# adds posts section into admin page
admin.site.register(Post)
