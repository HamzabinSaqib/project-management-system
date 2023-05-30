from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'authentication/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('authentication:home')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('authentication:login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'authentication/sign_up.html', context)
