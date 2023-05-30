from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(req):
    return render(req, 'authentication/home.html')

def login_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('base:home')
        else:
            messages.error(req, 'Invalid Username or Password')
    return render(req, 'authentication/login.html')

def logout_view(req):
    logout(req)
    return redirect('authentication:home')

def sign_up(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Account created successfully. You can now log in.')
            return redirect('authentication:login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(req, 'authentication/sign_up.html', context)
