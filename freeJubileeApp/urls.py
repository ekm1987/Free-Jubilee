from django.urls import path
from . import views


app_name = 'freeJubileeApp'

urlpatterns = [
    # free-jubilee/
    path('', views.IndexView.as_view(), name='index'),
    # free-jubilee/1
    path('<int:pk>/event', views.EventView.as_view(), name='event'),
    path('new-event/', views.AddEventView.as_view(), name='newEvent'),
    # free-jubilee/my-account
    path('my-account/', views.account, name='account'),
    ]