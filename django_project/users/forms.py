from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile #imported to update picture

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
        forms.EmailField: uses email that is default from django
    output:
        Can change the username and email
    """
    email = forms.EmailField()

    class Meta:
        """
        args:
            forms.ModelForm:
        input:
            model: once form.save(), saves it to user
            fields: this is showing the type of fields that are asked from the user
        output:
            saves information
        """
        model = User #user model will be affected, once validate, User is created
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    args:
        form.ModelForm: access information stored in database
    input:
        none
    output:
        change image on page
    """
    class Meta:
        """
        inputs:
            model: targets the profile of the user to save information
        field = changing the image
        """
        model = Profile
        fields = ['image']
