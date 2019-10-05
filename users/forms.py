from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MinLengthValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.forms import ModelForm, PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

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