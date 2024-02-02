from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .models import *
from vendors.models import *



def logoutUser(request):
    logout(request)
    return redirect('user_login')

def user_home(request):
    if request.user.is_authenticated:
        categories_list = categories.objects.all()
        venues = VendorProfile.objects.all()

        context = {'categories_list':categories_list,'venues':venues}
        return render(request, 'usr_home.html',context)
    else:
        return redirect('user_login')

def booking_details(request):
    return render(request, 'usr_bookings.html')

def venue_details(request):
    return render(request, 'usr_venue_details.html')

def user_profile(request):
    return render(request, 'usr_profile.html')


def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        # Create a new Django user
        user = User.objects.create_user(username=email, password=password)
        
        # Create a user profile associated with the new user
        profile = UserProfile.objects.create(user=user, name=name, phone_number=phone_number)
        profile.save()
        
        return redirect('user_login') 
    else:
        return render(request, 'usr_register.html')
    


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=email, password=password)

        if user is not None:
            # Check if the user exists in UserProfile
            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                # If user profile does not exist, render login page with error
                return render(request, 'usr_login.html', {'error_message': 'User profile does not exist'})

            # User is authenticated and has a profile, log them in
            login(request, user)
            return redirect('user_home')  # Adjust the URL name as needed
        else:
            # Authentication failed, display error message
            return render(request, 'usr_login.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login form template
        return render(request, 'usr_login.html')

