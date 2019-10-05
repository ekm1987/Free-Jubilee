from django.forms import ModelForm
from .models import Event
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time']