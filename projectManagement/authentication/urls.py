from django.urls import path
from . import views
from . views import check_username

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign-up/', views.sign_up, name='signup'),
    path('check-username/', views.check_username, name='check_username'),
]
