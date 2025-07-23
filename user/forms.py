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
from .models import Notifications

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['user', 'message', 'read_status']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'read_status': forms.CheckboxInput(),
        }
