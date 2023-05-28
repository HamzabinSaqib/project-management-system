
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import datetime
import uuid

# Create your models here.

class Project(models.Model):
    
    projID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
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
    
