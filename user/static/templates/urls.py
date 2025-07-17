from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.sidebar_view, name='profile'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('sidebar/', views.sidebar_view, name='sidebar'),  # from earlier
    path('dept/', views.dept_view, name='dept'),  # this one is for your dept.html
]

from django.urls import path
from . import views

urlpatterns = [
    path('sidebar/', views.sidebar_view, name='sidebar'),  # already added
    path('dept/', views.dept_view, name='dept'),            # already added
    path('update/', views.update_profile_view, name='update'),  # this line is new
]
