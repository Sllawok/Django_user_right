from django import forms
from .models import ArticlesUser
from django.contrib.auth.forms import UserCreationForm


class  RegistrationUserForm(UserCreationForm):

    class Meta:
        model = ArticlesUser
        #fields = '__all__'
        fields = ('username', 'password', 'email')
        # exclude = ('tags')