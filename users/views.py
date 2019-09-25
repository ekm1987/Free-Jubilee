from django.views import generic
from .models import CustomUser


class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/account.html'
    context_object_name = 'user'