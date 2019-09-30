from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm, UserChangeForm



class AccountView(generic.DetailView):
  model = CustomUser
  template_name = 'users/account.html'
  context_object_name = 'user'

class Register(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy("freeJubileeApp:index")
  template_name = "registration/register.html"

class ChangeUser(generic.UpdateView):
  form_class = UserChangeForm
  success_url = reverse_lazy('changeUser')
  template_name = 'changeUser.html'