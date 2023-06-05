from django.forms import inlineformset_factory
from django import forms
from .models import Project, Task, Assignee, Resource, Finances

class CreateProjectForm(forms.ModelForm):
    projName = forms.CharField(label="Name", max_length=50)
    projDesc = forms.CharField(label="Description", required=False, widget=forms.Textarea)
    Status_choices = [
        ('In Progress', 'In Progress'), 
        ('On Hold', 'On Hold'), 
        ('Completed', 'Completed'), 
        ('Cancelled', 'Cancelled'), 
        ('Overdue', 'Overdue'), 
        ('Inactive', 'Inactive')
    ]
    projStatus = forms.ChoiceField(label="Status", choices=Status_choices)
    dueDate = forms.DateTimeField(label="Due Date", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    endDate = forms.DateTimeField(label="End Date", required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Project
        fields = ('projName', 'projDesc','dueDate','endDate','projStatus',)


class CreateTaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=Assignee.objects.all(), empty_label=None)

    class Meta:
        model = Task
        fields = ['taskName', 'taskDesc', 'taskStatus', 'assigned_to', 'project', 'dueDate']

CreateTaskFormSet = inlineformset_factory(Project, Task, form=CreateTaskForm, extra=1)


class ManageResourceForm(forms.ModelForm):
    availableHours = forms.IntegerField(min_value=0)
    plannedEffort = forms.IntegerField(min_value=0)
    actualEffort = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Resource
        fields = ['availableHours', 'plannedEffort', 'actualEffort']


class ManageFinanceForm(forms.ModelForm):
    revenue = forms.IntegerField(min_value=0)
    cost = forms.IntegerField(min_value=0)
    margin = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Finances
        fields = ['revenue', 'cost', 'margin']
        
        
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
    resourceForm = ManageResourceForm()
    financeForm = ManageFinanceForm()
    taskForm = CreateTaskForm()
    
    class Meta:
        model = Project
        fields = ['projStatus']
