from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .models import *
from users.models import *

def is_vendor(request):
    user_id = request.user.id
    if VendorProfile.objects.filter(user=user_id).exists():
        return
    else:
        logout(request)
        return redirect('vendor_login')


def vendor_home(request):
    vendor = VendorProfile.objects.get(user=request.user.id)
    all_booking = bookings.objects.filter(vendor=vendor)
    context = {'all_booking':all_booking}
    return render(request, 'vendor_home.html',context)

def booking_pricing(request,pk):
    if request.method == 'POST':
        advance = request.POST.get('advance')
        total = request.POST.get('total')
        booking = bookings.objects.get(id=pk)
        booking.Total = total
        booking.billed = True
        booking.Advance = advance
        booking.save()

    return redirect('vendor_home')


def rejectBooking(request,pk):
    booking = bookings.objects.get(id=pk)
    booking.delete()
    return redirect('vendor_home')
    


def logoutVendor(request):
    logout(request)
    return redirect('vendor_login')


def vendor_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        category = request.POST.get('category')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')
        username = request.POST.get('username')
        password = request.POST.get('password')
        ac = request.POST.get('acCheckbox') == 'on'
        capacity = request.POST.get('capacity')
        location = request.POST.get('location')

        if User.objects.filter(email=email).exists():
            return render(request, 'vendor_register.html', {'error_message': f'Email address {email} is already registered.'})
        else:
            # Create a new Django user
            user = User.objects.create_user(username=username,email=email ,password=password)
            # Create a user profile associated with the new user
            profile = VendorProfile.objects.create(user=user, business_name=name, city=city,desc=desc, phone_number=phone_number,image=image,category=category,ac=ac,capacity=capacity,location=location)
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

