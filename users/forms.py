from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',)


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',)