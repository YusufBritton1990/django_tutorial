from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    """
    UserCreationForm: Inherits from UserCreationForm, defined in forms.py
        * it is UserCreationForm + a email field + crispy_forms
        UserCreationForm: creates a form for users to input information
        crispy_forms: app added in django_project/urls.py
            This made the form look better and handles error messages

    register.html

    in the registers.html file, you can extend files from other apps
    template folders

    register.html is using a CSRF token (Cross Reference forgery token) will
    protect our site from certain attacks

    form variable will create form. using "as_p" method will add p tags, making
    the page look more presentable

    #request is the HTTP request that passes information
    #clean_data converts form into a python form
    #name given in blog>urls.py


    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #This POST method is the username and two passwords
        if form.is_valid():
            form.save() #saves the form
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now logged in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """
    decorator:
        login_required: only display this page when successfully logged in.
        if unsuccessful, will redirect based on project settings
    args:
        request: HTTP request for this page

    input:
        if request.method == 'POST': checking to see if information is posted

            u_form: User form, defined in forms. grants user access to update
            username and email from the front end

                request.POST: This will post the information

                instance=request.user: This will show the current user in the
                form. This will show the email and username

            p_form: Profile form, defined in forms. grants user access to
            update profile picture

                request.POST: This will post the information

                request.FILES: This is the image itself

                instance=request.user: This will show the current user in the
                form. This will show the profile picture name
        else:
            Default information, awaiting to have data posted


    output:
        renders profile html with picture, and forms to update picture,
        username, and email. Once updated, it will redirect to profile page
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save() #saves the form
            p_form.save()
            messages.success(request, f'Your account has been Updated! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)

# message.debug
# message.info
# message.success
# message.warning
# message.error
