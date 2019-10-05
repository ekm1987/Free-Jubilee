from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # users/1
    path('<int:pk>/', views.AccountView.as_view(), name='account_info'),
    path('register/', views.Register.as_view(), name='register'),
]