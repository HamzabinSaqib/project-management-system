from django.shortcuts import render
from . models import Project

def login(req):
    return render(req, 'base/login.html')

def home(req):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(req, 'base/home.html', context)

def project(req, pk):
    project = Project.objects.get(projID=pk)
    context = {'project': project}
    return render(req, 'base/project.html', context)