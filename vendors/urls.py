# venues/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.vendor_register, name='vendor_register'),
    path('login/', views.vendor_login, name='vendor_login'),
    path('', views.vendor_home, name='vendor_home'),
]
