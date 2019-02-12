from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user created on blog

# Models are used to create databases
class Post(models.Model):
    """
    CharField: single line of text
        max_length=100: is the amount of character allowed

    TextField: multiple lines of text

    DateTimeField: use of datetime objects
        auto_now=True: when the post  updates
        auto_now_add=True: This will set time to when it first created
        default=timezone.now: display current time based on timezone

    author: one to many relationship (one user can have multiple post)
    ForeignKey: this will call in the User
        on_delete=models.CASCADE: if user is deleted, it will delete all of their posts
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # dunder (double underscore method)
    # When the object is called from Post.objects.all(), it will show the title rather than the default "Post object"
    def __str__(self):
        return self.title
