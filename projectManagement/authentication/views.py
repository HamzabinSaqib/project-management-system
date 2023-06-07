from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
import json

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        if password == conf_password:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created! You can now log in.')
            return redirect('authentication:login')
    
    return render(request, 'authentication/sign_up.html')

def check_username(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        username = body_data.get('username')
        available = True if not User.objects.filter(username=username).exists() else False
        print(f"\nAvailable: {available}\n")
        return JsonResponse({'available': available})
    return JsonResponse({'error': 'Invalid request method.'})