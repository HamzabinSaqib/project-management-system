from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Project, Task, Assignee, Assignment, Resource, Finances

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer()
    class Meta:
        model = Project
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Task
        fields = '__all__'

class AssigneeSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Assignee
        fields = '__all__'
class AssignmentSerializer(serializers.ModelSerializer):
    assignee = AssigneeSerializer()
    task = TaskSerializer()
    class Meta:
        model = Assignment
        fields = '__all__'
class ResourceSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Resource
        fields = '__all__'
        
class FinancesSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Finances
        fields = '__all__'