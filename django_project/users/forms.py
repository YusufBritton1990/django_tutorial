from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inherit the default user form
    """
    args:
        UserCreationForm: django default form. has username and password
    input:
        email: adding email field to form
        Meta class: saves changes to django's User section
    output:
        Form for user creation that saves to Django's User model
    """
    email = forms.EmailField() #this adds the email field to the default form

    class Meta:
            """
            model: once form.save(), saves it to user
            fields: this is showing the type of fields that are asked from the user
            """
            model = User #user model will be affected, once validate, User is created
            fields = ['username', 'email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    """args:
        forms.ModelForm:
    input:
        model: once form.save(), saves it to user
        fields: this is showing the type of fields that are asked from the user
    output:

    """
    model = User #user model will be affected, once validate, User is created
    fields = ['username', 'email',]
