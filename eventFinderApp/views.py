from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from .tokens import account_activation_token




class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related()
        )

    def get_context_data(self, **kwargs):  # WIP
        context = super().get_context_data(**kwargs)
        for index,event in enumerate(self.object_list):
            context[index] = [
                event.categories.all()[:3]
            ]
        # for i in context:
        #     print(context[i])
        return context

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class AddEventView(generic.CreateView):
    # using the create view we can just give it the variables 
    # as the functionaity is already built in!
    form_class = EventForm
    context_object_name = 'eventform'
    template_name = 'eventFinderApp/createEvent.html'
    success_url = reverse_lazy('eventFinderProject:index')
    # we have to use reverse_lazy so that urls.py can load our class
    # and not get stuck in a recursive loop 

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

def account(request):
    return render(request, 'users/account.html')

def signup(request):
    return render(request, 'users/signup.html')