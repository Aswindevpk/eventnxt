# venues/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.vendor_register, name='vendor_register'),
    path('login/', views.vendor_login, name='vendor_login'),
    path('logout/',views.logoutVendor, name='logoutVendor'),
    path('reject_booking/<str:pk>',views.rejectBooking, name='rejectBooking'),
    path('booking-pricing/<str:pk>', views.booking_pricing, name='booking_pricing'),
    path('', views.vendor_home, name='vendor_home'),
]


