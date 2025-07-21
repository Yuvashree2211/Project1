from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import Users, Roles

def index_view(request):
    return render(request, 'index.html')

def role_choice_view(request):
    return render(request, 'rolechoice.html')

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

def payroll_view(request):
    return render(request, 'payroll.html')


def announcements_view(request):
    return render(request, 'announcements.html')


def documents_view(request):
    return render(request, 'documents.html')

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


def welcome_page(request):
    return render(request, 'welcome.html')

def redirect_to_welcome(request):
    return redirect('welcome')


def register_view(request):
    return render(request, 'register.html')

def attend_view(request):
    return render(request, 'Attend.html')

def statistics_view(request):
    return render(request, 'statistics.html')
