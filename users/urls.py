from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/',views.user_profile, name='user_profile'),
    path('venue_details/',views.venue_details, name='venue_details'),
    path('', views.user_home, name='user_home'),
]
