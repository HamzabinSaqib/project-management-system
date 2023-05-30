from django.urls import path
from . import views

app_name = 'managment'

urlpatterns = [
  path('project/<str:pk>/', views.manage_project, name='manage')
]