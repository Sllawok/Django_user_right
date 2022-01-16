from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import RegistrationUserForm
from django.views.generic import CreateView
from .models import ArticlesUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateView(CreateView):
    model = ArticlesUser
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('articles:index')


