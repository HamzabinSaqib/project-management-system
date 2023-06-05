from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.home, name='home'),
    path('project/<str:pk>/', views.project, name='project'),
    path('new/', views.create_project, name='new_Project'),
    path('project/<str:pk>/manage/', views.manage_project, name='manage_Project'),
    path('delete/<str:pk>/', views.delete_project, name='del_project')
]