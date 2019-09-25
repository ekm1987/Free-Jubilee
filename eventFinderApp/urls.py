from django.urls import path
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/event', views.EventView.as_view(), name='event'),
    path('new-event/', views.AddEventView.as_view(), name='newEvent'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/signup
    path('signup/', views.signup, name='signup'),
    ]