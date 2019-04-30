from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    save: Note: this is overwriting the original save method. We are doing this
    to have the ability to resize images
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        args:
            self: class self parameter, targets the data
        input:
            super().save(): uses the save global variable, which save data into
            the database
            img: store the instance of the image path
        output:
            edited save function for profile pics that will resize big images
        """
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
