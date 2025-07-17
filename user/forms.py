from django import forms
from .models import Users

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['full_name', 'email', 'phone', 'password', 'profile_picture']
