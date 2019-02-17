from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """docstring for ."""
    email = forms.Emailfield()

    class Meta:
        """docstring for Meta."""
            model = User #user model will be affected
            fields = ['username', 'email','password1','password2']
