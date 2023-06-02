from django.forms import inlineformset_factory
from django import forms
from .models import Project, Task, Assignee

class CreateProjectForm(forms.ModelForm):
  projName = forms.CharField(label="Name", max_length=50)
  projDesc = forms.CharField(label="Description", required=False, widget=forms.Textarea)
  Status_choices = [('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue'), ('Inactive', 'Inactive')]
  projStatus = forms.ChoiceField(label="Status", choices=Status_choices)
  dueDate = forms.DateTimeField(label="Due Date", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
  endDate = forms.DateTimeField(label="End Date", required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
  
  
  class Meta:
    model = Project
    fields = ('projName', 'projDesc','dueDate','endDate','projStatus',)


class ManageTaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=Assignee.objects.all(), empty_label=None)

    class Meta:
        model = Task
        fields = ['taskName', 'taskDesc', 'taskStatus', 'assigned_to', 'project', 'dueDate']

ManageTaskFormSet = inlineformset_factory(Project, Task, form=ManageTaskForm, extra=1)

class ManageProjectForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Overdue', 'Overdue'),
        ('Inactive', 'Inactive')
    ]

    projStatus = forms.ChoiceField(choices=STATUS_CHOICES)
    project_availableHours = forms.IntegerField(min_value=0)
    class Meta:
        model = Project
        fields = ['projStatus', 'project_availableHours',]
