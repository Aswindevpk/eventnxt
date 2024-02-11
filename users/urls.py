from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path('profile/',views.user_profile, name='user_profile'),
    path('venue_details/<str:pk>',views.venue_details, name='venue_details'),
    path('search_venue',views.search_venue, name='search_venue'),
    path('booking_details/',views.booking_details, name='booking_details'),
    path('booking_request/',views.booking_request, name='booking_request'),
    path('', views.user_home, name='user_home'),
]
