from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    """
    UserCreationForm: creates a form for users to input information

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
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# message.debug
# message.info
# message.success
# message.warning
# message.error
