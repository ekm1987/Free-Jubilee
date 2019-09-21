from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views
from . import views as core_views
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/event', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/signup
    path('signup/', views.signup, name='signup'),
    # event-finder/signup
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    ]