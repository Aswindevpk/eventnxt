from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm


def home(request):
    return render(request, 'usr_home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = RegistrationForm()
    return render(request, 'usr_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'usr_login.html', {'form': form})



