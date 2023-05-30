from django import forms
from .models import Project

class CreateProjectForm(forms.ModelForm):
  Status_choices = [('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue'), ('Inactive', 'Inactive')]
  projStatus = forms.ChoiceField(choices=Status_choices)
  
  class Meta:
    model = Project
    fields = ('projName', 'projDesc','dueDate','endDate','projStatus',)

class ProjectForms(forms.Form):
  Status_choices = [('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue'), ('Inactive', 'Inactive')]
  
  projStatus = forms.CharField(widget=forms.Select(choices=Status_choices))
  task_name = forms.CharField()
  task_desc = forms.CharField()
  taskStatus = forms.CharField(widget=forms.Select(choices=Status_choices))
  assigned_to = forms.CharField()
  project_availableHours = forms.IntegerField(min_value=0)
  effort_so_far = forms.IntegerField(min_value=0)
  budget_spent_so_far = forms.IntegerField(min_value=0)