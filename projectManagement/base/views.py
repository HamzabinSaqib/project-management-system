from django.shortcuts import render

def login(req):
    return render(req, 'login.html')

def home(req):
    return render(req, 'home.html')
