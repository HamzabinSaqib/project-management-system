from django.contrib import admin

# Register your models here.

from .models import Project, Task, Assignee, Assignment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Assignee)
admin.site.register(Assignment)
