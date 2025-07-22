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
from django.urls import path, include
from user.views import user_signup,signin_view, dashboard_view

from user.views import index_view, role_choice_view, login_page,user_signup,signin_view, dashboard_view,welcome_page,early_view,employe_view,logout_view


from django.urls import path, include
from user.views import *
from .views import index_view, role_choice_view
from . import views 

urlpatterns = [
   
    path('', login_page, name='login'),  # Set root URL to show login page
    path('', index_view, name='index'),
    path('rolechoice/', signin_view, name='role_choice'),
    path('signup/',user_signup, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('update/', views.update_view, name='update'),
    path('department/', views.department_view, name='department'),
    path('profile/', views.profile_view, name='profile'),
    path('latecomers/', views.latecomers_view, name='latecomers'),
    path('payroll/', views.payroll_view, name='payroll'),
    path('announcements/', views.announcement_view, name='announcements'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('documents/', views.document_view, name='documents'),
    path('employee-login/', views.employee_login, name='employee_login'),
    path('supervisor-login/', views.supervisor_login, name='supervisor_login'),
    path('add_payroll/', views.add_payroll_view, name='add_payroll'),
    path('login/', views.redirect_to_welcome, name='login'),
    path('welcome/', views.welcome_page, name='welcome'),
     path('Attend/', views.Attend_view, name='Attend'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('early/', views.early_view, name='early'),
    path('employe/', views.employe_view, name='employe'),
    path('logout/', views.logout_view, name='logout'),
    path('leave/', views.leave_view, name='leave'),
    path('notification/', views.notification_view, name='notification'),
    path('task/', views.task_view, name='task'),
]


