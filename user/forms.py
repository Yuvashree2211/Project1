from django import forms
from .models import Users

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['full_name', 'email', 'phone', 'password', 'profile_picture']

from django import forms
from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['user', 'month', 'base_salary', 'bonus', 'deductions', 'net_pay', 'status', 'paid_on']
        widgets = {
            'month': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter month (e.g., July 2025)'}),
            'base_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'bonus': forms.NumberInput(attrs={'class': 'form-control'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control'}),
            'net_pay': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Paid', 'Paid'),
                ('Pending', 'Pending'),
                ('Processing', 'Processing'),
            ]),
            'paid_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        
from django import forms
from .models import Tasks, Users

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['assigned_to', 'assigned_by', 'title', 'description', 'status', 'due_date']
        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'assigned_by': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(choices=[
                ('Pending', 'Pending'),
                ('Completed', 'Completed'),
                ('Overdue', 'Overdue'),
            ], attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = Users.objects.all()
        self.fields['assigned_by'].queryset = Users.objects.all()



from django import forms
from .models import Leaves

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = ['user', 'start_date', 'end_date', 'reason', 'leave_type', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
            'leave_type': forms.TextInput(attrs={'placeholder': 'Sick, Casual, Paid...'}),
            'status': forms.TextInput(attrs={'placeholder': 'Pending/Approved/Rejected'}),
        }

from django import forms
from .models import Notifications

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['user', 'message', 'read_status']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'read_status': forms.CheckboxInput(),
        }

from django import forms
from .models import Announcements

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }

from django import forms
from .models import Documents

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['user', 'doc_type', 'file_path']

