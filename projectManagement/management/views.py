from django.shortcuts import render, get_object_or_404, redirect
from base.models import Project, Task, Finances, Assignee, Assignment, Resource
from base.forms import ManageProjectForm
# Create your views here.

def manage_project(request, pk): #(request, project_id)
  project = Project.objects.get(id=pk)
  form = ManageProjectForm(instance=project)
  if request.method == "POST":
    form = ManageProjectForm(request.POST)
    if form.is_valid:
      print(form.cleaned_data)
      # project.projStatus = form.changed_data['projStatus']
      # project.projStatus = form.changed_data['projStatus']
      # project.projStatus = form.changed_data['projStatus']
      
  context={
    "project":project,
    "form":form
  }
  return render(request, "management/manage_proj.html", context)

#! KINDA BROKE THIS 
#! WILL FIX TOMORROW