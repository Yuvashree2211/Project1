from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .forms import UserSignupForm
from .models import Users, Roles

def index_view(request):
    return render(request, 'index.html')

def role_choice_view(request):
    return render(request, 'rolechoice.html')

def login_page(request):
    return render(request, 'loginpage.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])

            # Set default role
            default_role = Roles.objects.filter(role_name='User').first()
            user.role = default_role

            user.status = "Active"
            user.save()
            return redirect('login')  # or any success page
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})



def signin_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = Users.objects.get(email=email)
            username = user_obj.username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, "signin.html", {"error": "Invalid credentials"})
        except Users.DoesNotExist:
            return render(request, "signin.html", {"error": "User not found"})

    return render(request, "signin.html")

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


def payroll_view(request):
    return render(request, 'payroll.html')

def announcements_view(request):
    return render(request, 'announcements.html')

def documents_view(request):
    return render(request, 'documents.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def register_view(request):
    return render(request, 'register.html')


def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def notification_view(request):
    return render(request, 'notification.html')
def attendence_view(request):
    return render(request, 'attendence.html')
def task_view(request):
    return render(request, 'task.html')
def leave_view(request):
    return render(request, 'task.html')