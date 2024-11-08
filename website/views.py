from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User authenticated:", user.username)
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            print("Failed login attempt")
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    return render(request, 'home.html')

def logout_user(request):
    logout(request)  # Use Django's logout function here
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')  # Ensure template file is correctly named
