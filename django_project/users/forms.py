from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #inherit the default user form
    """docstring for ."""
    email = forms.EmailField() #this adds the email field to the default form

    class Meta:
            """
            model: once form.save(), saves it to user
            fields: this is showing the type of fields that are asked from the user
            """
            model = User #user model will be affected, once validate, User is created
            fields = ['username', 'email','password1','password2']
