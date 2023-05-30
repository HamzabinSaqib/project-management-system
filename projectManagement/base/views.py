from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Project

@login_required(login_url='authentication:login')
def home(req):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(req, 'base/home.html', context)

@login_required(login_url='authentication:login')
def project(req, pk):
    project = Project.objects.get(projID=pk)
    context = {'project': project}
    return render(req, 'base/project.html', context)

