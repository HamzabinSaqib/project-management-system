from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
  path('base/home/<str:pk>/manage/', views.manage_project, name='management')
]