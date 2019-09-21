from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

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

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email_confirmed = models.BooleanField(default=False)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
