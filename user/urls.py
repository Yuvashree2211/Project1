"""
URL configuration for emp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import index_view, role_choice_view, login_page, user_signup,signin_view, dashboard_view
from django.urls import path, include
from user.views import *
from . import views

urlpatterns = [
    path('', index_view, name='index'),


 

   
    path('', login_page, name='login'),  # Set root URL to show login page
    path('index/', index_view, name='index'),
    path('rolechoice/', role_choice_view, name='role_choice'),
    path('signup/',user_signup, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('update/', views.update_view, name='update'),
    path('department/', views.department_view, name='department'),
    path('profile/', views.profile_view, name='profile'),
]
