from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.home, name='home'),
    path('project/<str:pk>/', views.project, name='project'),
    path('new/', views.create_project, name='new_Project'),
    path('manage/', include('management.urls', namespace='management')),
    path('delete/<str:pk>/', views.project_delete, name='project_delete')
]