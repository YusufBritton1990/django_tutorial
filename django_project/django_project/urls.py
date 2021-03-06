"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #Will be able to use standard, bootstrap login views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views #import view directly into project


# Upon opening the app, it will try to run either admin or blog.
#If the URL contains blog (User typing in the site), it will run include (root folder) than look for blog
#run urls

#Once a user type it blog, it will screch in blog>urls for futher processing
# For logout path, if no template_name is set, it will default to using django's admin page

"""
paths:
    admin: connection to admin site. default route
    register: sign up a new user. function view
    profile: look at logged in user profile. function view
    login: . Class view
    logout: . Class view
    password_reset. Class view
    password_reset_done: success message, stating email was sent. Class view
    password-reset-confirm: confirm the user and security token. Class view
    '': blog home page. this page is the index
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
    name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
    name='logout'),

    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
    name='password_reset'),

    path('password-reset/done',
    auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
    name='password_reset_complete'),

    path('', include('blog.urls')),
]

# Only adding in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
