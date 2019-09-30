from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MinLengthValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.forms import ModelForm, PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Valid email address required.')
    re_password = forms.CharField(max_length=128, widget=forms.PasswordInput, validators=[validate_password], label='Re-enter password')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for re_password, field in self.fields.items():
            field.required = True
        password_field = self.fields['password']
        password_field.validators.append(MinLengthValidator(limit_value=8))

    def clean(self):
        super(CustomUserCreationForm, self).clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if not password == re_password:
            self.add_error('re_password', 'Passwords must match')
        password.save()

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 're_password',)
        widgets = {
            'password': PasswordInput()
        }

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',)