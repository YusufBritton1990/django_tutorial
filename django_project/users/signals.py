from django.db.models.signals import post_save #apps ability to save new users
from django.contrib.auth.models import User
from django.dispatch import receiver #making receiver
from .models import Profile #when we make a user, make a profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    receiver decorater:
        post_save: a signal. once a user is saved, create_profile gets User info
        sender: this will be the user informaion
        This decorater is passed in with create_profile

    Imports:
        All: defined when passed with receiver decorater, implecitly
        sender: passed with receiver
        instance: once the user exist. passed in from @receiver
        created: if user is created, make a profile to match. from @receiver
        kwargs:
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    receiver decorater:
        post_save: once the information is posted
        sender: this will be the user informaion
        This decorater is passed in with create_profile

    Imports:
        All: defined when passed with receiver decorater, implecitly
        sender: passed with receiver
        instance: will update profile
        kwargs:
    """
    instance.profile.save()
