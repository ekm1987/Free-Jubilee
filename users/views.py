from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, UserChangeForm


@login_required
def home(request):
    return render(request, 'freeJubileeApp/index.html')

class AccountView(generic.DetailView):
  model = CustomUser
  template_name = 'users/account.html'
  context_object_name = 'user'

class Register(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy("freeJubileeApp:index")
  template_name = "registration/register.html"

  def register(self, request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class ChangeUser(generic.UpdateView):
  form_class = UserChangeForm
  success_url = reverse_lazy('changeUser')
  template_name = 'changeUser.html'

