from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .models import *
from vendors.models import *
from django.db.models import Q



def logoutUser(request):
    logout(request)
    return redirect('user_login')

def user_home(request):
    if request.user.is_authenticated:
        venues = VendorProfile.objects.all()
        context = {'venues':venues}
        return render(request, 'usr_home.html',context)
    else:
        return redirect('user_login')
    
def search_venue(request):
    query = request.GET.get('query')
    if query:
        results = VendorProfile.objects.filter(Q(business_name__icontains=query) | Q(category__icontains=query))
    else:
        results = VendorProfile.objects.none()
    context = {'venues':results}
    return render(request, 'usr_home.html',context)

def booking_details(request):
    user = UserProfile.objects.get(user=request.user.id)
    all_booking = bookings.objects.filter(user=user)
    context = {'all_booking':all_booking}
    return render(request, 'usr_bookings.html',context)

def cancel_booking(request,pk):
    booking = bookings.objects.get(id=pk)
    booking.delete()
    return redirect('booking_details')

def confirm_booking(request,pk):
    booking = bookings.objects.get(id=pk)
    booking.paid = True
    booking.save()
    return render(request, 'booking_confirm.html')


def pay_advance(request,pk):
    booking = bookings.objects.get(id=pk)
    context = {'booking':booking}
    return render(request, 'payment_gateway.html',context)


def booking_request(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        user = request.POST.get('user')
        venue = request.POST.get('venue')
        persons = request.POST.get('persons')
        booking = bookings.objects.create(date=date,user_id=user,vendor_id=venue,persons=persons)
        booking.save()
        booking_number = booking.id
        context = {'booking_number':booking_number}
    
    return render(request, 'booking_sucess.html',context )

def venue_details(request,pk):
    venue = VendorProfile.objects.get(id=pk)
    user = UserProfile.objects.get(user = request.user.id)

    context ={'venue':venue, 'user':user}
    return render(request, 'usr_venue_details.html',context)

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

