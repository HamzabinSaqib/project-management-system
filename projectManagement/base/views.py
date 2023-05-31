from django.shortcuts import render, redirect
from . models import Project
from .forms import CreateProjectForm
def login(req):
    return render(req, 'base/login.html')

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


def create_project(request):
    form = CreateProjectForm()
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            # project_name = form.cleaned_data
            print('The form is valid')
            print(form.cleaned_data)
            name = form.cleaned_data['projName']
            desc = form.cleaned_data['projDesc']
            due = form.cleaned_data['dueDate']
            end = form.cleaned_data['endDate']
            status = form.cleaned_data['projStatus']
            Project.objects.create(
                projName = name,
                projDesc = desc,
                dueDate = due,
                endDate = end,
                projStatus = status,
            )
            print('New Project created')
            return redirect("/home")
    context = {
        "form":form
    }
    return render(request, "base/project_creation.html", context)

def project_delete(request, pk):
    project = Project.objects.get(projID=pk)
    project.delete()
    return redirect("/home")