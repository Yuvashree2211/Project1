from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import Roles,Payroll
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
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Users  # Assuming this is your custom user model
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Payroll
from user.models import Users  # Adjust import as per your structure

def payroll_view(request):
    if request.method == 'POST':
        try:
            user = Users.objects.get(id=request.POST.get('user_id'))
            month = request.POST.get('month')
            base_salary = float(request.POST.get('base_salary', 0))
            bonus = float(request.POST.get('bonus', 0))
            deductions = float(request.POST.get('deductions', 0))
            net_pay = float(request.POST.get('net_pay', base_salary + bonus - deductions))
            status = request.POST.get('status')
            paid_on = request.POST.get('paid_on')

            Payroll.objects.create(
                user=user,
                month=month,
                base_salary=base_salary,
                bonus=bonus,
                deductions=deductions,
                net_pay=net_pay,
                status=status,
                paid_on=paid_on
            )
            users= Users.objects.all()
            
            messages.success(request, "Payroll added successfully.")
            return redirect('payroll',{'users': users})
        except Users.DoesNotExist:
            messages.error(request, "Selected user not found.")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    # Get all payroll entries and users for the form
    payrolls = Payroll.objects.select_related('user').order_by('-paid_on')
    users = Users.objects.all()
    return render(request, 'payroll.html', {
        'payrolls': payrolls,
        'users': users
    })
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Users

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        context = {'email': email}  # For repopulating email field on error

        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                # Set session
                request.session['user_id'] = user.id
                request.session['user_name'] = user.full_name
                request.session['user_role'] = user.role.role_name

                messages.success(request, f"Welcome, {user.full_name}!")

                role_name = user.role.role_name.upper()

                if role_name == 'ADMIN':
                    return redirect('admin_dashboard')
                elif role_name == 'SUPERVISOR':
                    return redirect('supervisor_dashboard')  # or another dashboard
                elif role_name == 'EMPLOYEE':
                    return redirect('dashboard')  # intern/employee dashboard
                else:
                    messages.error(request, "Unauthorized role.")
            else:
                messages.error(request, 'Invalid email or password.')

        except Users.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

        return render(request, 'signin.html', context)

    return render(request, 'signin.html')


from django.shortcuts import render, redirect

def dashboard_view(request):
    if 'user_id' not in request.session:
        return redirect('signin')

    context = {
        'user_name': request.session.get('user_name'),
    }
    return render(request, 'dashboard.html', context)


def admin_dashboard_view(request):
    if 'user_id' not in request.session:
        return redirect('signin')

    context = {
        'user_name': request.session.get('user_name'),
    }
    return render(request, 'admin.html', context)

def update_view(request):

    return render(request, 'update.html')

def department_view(request):
    return render(request, 'department.html')

from django.core.files.storage import FileSystemStorage

def profile_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('signin')

    try:
        user = Users.objects.select_related('role').get(id=user_id)
    except Users.DoesNotExist:
        return redirect('signin')

    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile_picture = request.FILES['profile_picture']
        user.profile_picture = profile_picture
        user.save()
        return redirect('profile')  # refresh the page

    return render(request, 'profile.html', {'user': user})


def latecomers_view(request):
    return render(request, 'user/latecomers.html')

def employee_login(request):
    return render(request, 'loginpage.html')

def supervisor_login(request):
    return render(request, 'log.html') 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserSignupForm
from .models import Roles
from django.shortcuts import render, redirect
from .models import Users, Roles
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password


def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role_name = request.POST.get('role')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        try:
            # Get the Role object based on selected dropdown value
            role = Roles.objects.get(role_name__iexact=role_name)

            # Hash the password
            hashed_password = make_password(password)

            # Create and save user
            user = Users.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                role=role,
                password=hashed_password,
                profile_picture=profile_picture,
                status="Active"
            )
            messages.success(request, 'Account created successfully!')
            return redirect('signin')  # or wherever you want to go after sign-up

        except ObjectDoesNotExist:
            messages.error(request, 'Selected role is invalid.')
        except IntegrityError:
            messages.error(request, 'User with this email already exists.')
        except Exception as e:
            messages.error(request, f'Something went wrong: {str(e)}')

    return render(request, 'signup.html')

def supervisor_dashboard_view(request):
    if 'user_id' not in request.session:
        return redirect('signin')

    context = {
        'user_name': request.session.get('user_name'),
    }
    return render(request, 'supervisor_dashboard.html', context)


def add_payroll_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        month = request.POST.get('month')
        base_salary = request.POST.get('base_salary')
        bonus = request.POST.get('bonus') or 0
        deductions = request.POST.get('deductions') or 0
        net_pay = request.POST.get('net_pay')
        status = request.POST.get('status')
        paid_on = request.POST.get('paid_on')

        try:
            user = Users.objects.get(id=user_id)
            Payroll.objects.create(
                user=user,
                month=month,
                base_salary=base_salary,
                bonus=bonus,
                deductions=deductions,
                net_pay=net_pay,
                status=status,
                paid_on=paid_on
            )
            messages.success(request, "Payroll added successfully.")
        except Users.DoesNotExist:
            messages.error(request, "User not found.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect('payroll')
    else:
        return redirect('payroll')

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

from .models import Notifications, Users
from .forms import NotificationForm
from django.utils import timezone

def notification_view(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.instance.created_at = timezone.now()
            form.save()
            messages.success(request, "Notification sent successfully.")
            return redirect('notification')
    else:
        form = NotificationForm()

    # Fetch all notifications
    notifications = Notifications.objects.select_related('user').order_by('-created_at')
    return render(request, 'notification.html', {
        'form': form,
        'notifications': notifications
    })


def task_view(request):
    return render(request, 'task.html')

def attendence_view(request):
    return render(request, 'attendence.html')
from django.shortcuts import render

def attendance(request):
    return render(request, 'attendance.html')

def leave(request):
    return render(request, 'leave.html')

from django.shortcuts import get_object_or_404

def mark_notification_read(request, pk):
    notification = get_object_or_404(Notifications, pk=pk)
    notification.read_status = True
    notification.save()
    messages.success(request, "Notification marked as read.")
    return redirect('notification')

def delete_notification(request, pk):
    notification = get_object_or_404(Notifications, pk=pk)
    notification.delete()
    messages.success(request, "Notification deleted.")
    return redirect('notification')

