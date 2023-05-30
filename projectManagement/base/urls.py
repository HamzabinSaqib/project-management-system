from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.home, name='home'),
    path('project/<str:pk>/', views.project, name='project'),
    path('new/', views.create_project, name='Create New Project'),
    path('manage/', include('managment.urls', namespace='managment'))
]