
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import uuid

# Create your models here.

class Project(models.Model):
    """Project Model"""
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    projID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projName = models.CharField(max_length=50)
    projDesc = models.TextField(null=True, blank=True)
    startDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    projStatus = models.CharField(max_length=20)
    
    def set_projStatus(self, stat: str): # In Progress - On Hold - Completed - Cancelled - Overdue - Inactive
        """Set Project Status"""
        self.projStatus = stat
        self.save()
    
    def set_dueDate(self, date: str): # 'YYYY-DD-MM HH:MM:SS'
        """Set Project Due Date"""
        self.dueDate = datetime.strptime(date, '%Y-%d-%m %H:%M:%S')
        
    def __str__(self):
        return self.projName
    
    def save(self, *args, **kwargs):
        if (self.projStatus == 'Completed' or self.projStatus == 'Cancelled') and not self.endDate:
            self.endDate = timezone.now()
        return super().save(*args, **kwargs)


class Task(models.Model):
    """Task Model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    taskID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    taskName = models.CharField(max_length=40)
    taskDesc = models.TextField(null=True, blank=True)
    startTime = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField()
    endTime = models.DateTimeField(null=True, blank=True)
    taskStatus = models.CharField(max_length=20)
    
    def set_taskStatus(self, stat: str): # In Progress - On Hold - Completed - Cancelled - Overdue - Inactive
        """Set Project Status"""
        self.taskStatus = stat
        self.save()
    
    def set_dueDate(self, date: str): # 'YYYY-DD-MM HH:MM:SS'
        """Set Project Due Date"""
        self.dueDate = datetime.strptime(date, '%Y-%d-%m %H:%M:%S')
        
    def __str__(self):
        return self.taskName
    
    def save(self, *args, **kwargs):
        if (self.taskStatus == 'Completed' or self.taskStatus == 'Cancelled') and not self.endTime:
            self.endTime = timezone.now()
        return super().save(*args, **kwargs)


class Assignee(models.Model):
    """Assignee Model"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    assigneeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assigneeName = models.CharField(max_length=25)
    
    def __str__(self):
        return self.assigneeName

class Assignment(models.Model):
    """Assignment Model"""
    assignee = models.ForeignKey(Assignee, on_delete=models.PROTECT) #! Will Raise Exception when related Assignee Deleted
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assignID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assignDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.assignID

class Resource(models.Model):
    pass

class Finances(models.Model):
    pass