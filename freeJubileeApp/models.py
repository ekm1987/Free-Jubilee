from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    venue = models.CharField(max_length=200, default='')
    categories = models.ManyToManyField('Category', related_name='events', blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
