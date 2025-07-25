
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


from django.urls import path, include
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index_view, name='index'),
     

    path('', include('user.urls')),  # Include your app's routes
    path('', views.login_page, name='login'),  # Set root URL to show login page
 
    path('rolechoice/', views.role_choice_view, name='role_choice'),
    path('signup/',views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('dashboard/',views.dashboard_view, name='dashboard'),
    path('update/', views.update_view, name='update'),
    path('department/', views.department_view, name='department'),
    path('profile/', views.profile_view, name='profile'), 
     
 
    path('attendance/', views.attendance, name='attendance'),
    path('leave/', views.leave_view, name='leave'),

]
