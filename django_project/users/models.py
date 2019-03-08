from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    user: using models' OneToOneField function, it is establishing a one-one
    relationship between the user and profile
        on_delete= When user is deleted, it will delete profile. if profile deleted,
        profile will stay

    image: this will be the profile picture
        default: default imgae
        upload_to: folder that will store picturs

    __str__ : Dunder (double underscore) method. used to initiate something
        f' : f string. This will dynamically display, in this case, the username
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
