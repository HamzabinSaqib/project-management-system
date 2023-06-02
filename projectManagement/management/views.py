from django.shortcuts import render, get_object_or_404, redirect
from base.models import Project, Task, Finances, Assignee, Assignment, Resource
from base.forms import ManageProjectForm
# Create your views here.


def manage_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ManageProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        form = ManageProjectForm(instance=project)
    
    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'managment/manage_proj.html', context)

