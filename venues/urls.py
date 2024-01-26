# venues/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.venue_login, name='login'),
    path('', views.home, name='home'),
    # Add other venue-related URL patterns
]