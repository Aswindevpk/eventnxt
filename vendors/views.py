from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *


def vendor_home(request):
    return render(request, 'vendor_home.html')


def vendor_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new Django user
        user = User.objects.create_user(username=username,email=email ,password=password)
        
        # Create a user profile associated with the new user
        profile = VendorProfile.objects.create(user=user, business_name=name, city=city, phone_number=phone_number)
        profile.save()
        
        return redirect('vendor_login') 
    else:
        return render(request, 'vendor_register.html')
    


def vendor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                vendor_profile = VendorProfile.objects.get(user=user)
            except VendorProfile.DoesNotExist:
                return render(request, 'vendor_login.html', {'error_message': 'User profile does not exist'})

            login(request, user)
            return redirect('vendor_home') 
        else:
            return render(request, 'vendor_login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'vendor_login.html')

