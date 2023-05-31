from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Project
from .forms import CreateProjectForm

@login_required(login_url='authentication:login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(projName__icontains=q)
    context = {'projects':projects}
    return render(request, 'base/home.html', context)

@login_required(login_url='authentication:login')
def project(request, pk):
    project = Project.objects.get(projID=pk)
    context = {'project': project}
    return render(request, 'base/project.html', context)

@login_required(login_url='authentication:login')
def create_project(request):
    form = CreateProjectForm()
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            manager_username = request.user.username
            mgr = User.objects.get(username=manager_username)
            # project_name = form.cleaned_data
            print('The form is valid')
            print(form.cleaned_data)
            name = form.cleaned_data['projName']
            desc = form.cleaned_data['projDesc']
            due = form.cleaned_data['dueDate']
            end = form.cleaned_data['endDate'] if 'endDate' in form.cleaned_data else None
            status = form.cleaned_data['projStatus']
            Project.objects.create(
                manager = mgr,
                projName = name,
                projDesc = desc,
                dueDate = due,
                endDate = end,
                projStatus = status,
            )
            print('New Project created')
            return redirect('base:home')
    context = {"form":form}
    return render(request, "base/project_creation.html", context)

@login_required(login_url='authentication:login')
def project_delete(request, pk):
    if request.method == "POST":
        project = Project.objects.get(projID=pk)
        project.delete()
    return redirect('base:home')
