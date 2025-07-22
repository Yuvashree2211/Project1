from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import Roles
from .forms import PayrollForm
def index_view(request):
    return render(request, 'index.html')

def role_choice_view(request):
    roles = Roles.objects.all()
    return render(request, 'rolechoice.html', {'roles': roles})

def login_page(request):
    return render(request, 'loginpage.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Users
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Users

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('dashboard')  # Change 'dashboard' to your desired redirect
            else:
                messages.error(request, 'Invalid email or password.')
        except Users.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'signin.html')


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, "dashboard.html")

def update_view(request):

    return render(request, 'update.html')

def department_view(request):
    return render(request, 'department.html')

def profile_view(request): 
    return render(request, 'profile.html')


def latecomers_view(request):
    return render(request, 'user/latecomers.html')

def employee_login(request):
    return render(request, 'loginpage.html')

def supervisor_login(request):
    return render(request, 'log.html') 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Users, Roles
from .forms import UserSignupForm

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])

            # Assign default role
            default_role = Roles.objects.filter(role_name='User').first()
            user.role = default_role
            user.status = "Active"
            user.save()

            # Redirect to register.html after successful signup
            return redirect('register')  # make sure 'register' is defined in urls.py
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})


def payroll_view(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll')
    else:
        form = PayrollForm()
    return render(request, 'payroll.html', {'form': form})

def announcement_view(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements.html', {'form': form})

def document_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()
    return render(request, 'documents.html', {'form': form})

def welcome_page(request):
    return render(request, 'welcome.html')

def redirect_to_welcome(request):
    return redirect('welcome')

def Attend_view(request):
    return render(request, 'Attend.html')

def statistics_view(request):
    return render(request, 'statistics.html')

def early_view(request):
    return render(request, 'early.html')

def employe_view(request):
    return render(request, 'employe.html')

def logout_view(request):
    return render(request, 'logout.html')

def leave_view(request):
    return render(request, 'leave.html')

def notification_view(request):
    return render(request, 'notification.html')

def task_view(request):
    return render(request, 'task.html')

def attendence_view(request):
    return render(request, 'attendence.html')
from django.shortcuts import render

def attendance(request):
    return render(request, 'attendance.html')

def leave(request):
    return render(request, 'leave.html')
