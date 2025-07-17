from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('departments/', views.dept_view, name='departments'),
    path('update/', views.update_view, name='update'),
]
