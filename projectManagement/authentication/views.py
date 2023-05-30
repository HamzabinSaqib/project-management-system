from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from base.models import Manager



def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:home')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            manager = Manager.objects.create(user=user)
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('authentication:login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})
