from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import Project
from .forms import ManageProjectForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
#! ======================================================== HOME =======================================================

@login_required(login_url='authentication:login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(projName__icontains=q)
    # Check if the user is a manager of any project
    is_manager = any(project.manager.username == request.user.username for project in projects)
    context = {'projects':projects, 'is_manager': is_manager, 'q': q}
    return render(request, 'base/home.html', context)

#! ====================================================== PROJECT ======================================================


@login_required(login_url='authentication:login')
def project(request, pk):
    project = Project.objects.get(projID=pk)
    context = {'project': project}
    return render(request, 'base/project.html', context)

#! =================================================== CREATE PROJECT ===================================================

@login_required(login_url='authentication:login')
def create_project(request):
    if request.method == "POST":
        manager_username = request.user.username
        mgr = User.objects.get(username=manager_username)
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        
        if start_date == "":
            start_date = None
        if due_date == "":
            due_date = None
            
        Project.objects.create(
            manager = mgr,
            projName = name,
            projDesc = desc,
            startDate = start_date,
            dueDate = due_date,
            projStatus = status,
        )
        return redirect('base:home')
    return render(request, "base/create_project.html")

#! =================================================== DELETE PROJECT ===================================================

@login_required(login_url='authentication:login')
def delete_project(request, pk):
    if request.method == "POST":
        project = Project.objects.get(projID=pk)
        project.delete()
    return redirect('base:home')

#! =================================================== MANAGE PROJECT ===================================================

@login_required(login_url='authentication:login')
def manage_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ManageProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('base:project', pk)  # Replace 'home' with the appropriate URL name
    else:
        form = ManageProjectForm(instance=project)
    
    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'base/manage_project.html', context)



def create_task(request, pk):
    pass