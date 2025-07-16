from django.contrib import admin
from .models import (
    Role, User, Department, JobPost, Attendance,
    Task, Leave, Payroll, Notification
)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name']
    search_fields = ['role_name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'role', 'status']
    search_fields = ['full_name', 'email']
    list_filter = ['role', 'status']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'department', 'posted_by', 'posted_at']
    list_filter = ['department', 'posted_at']
    search_fields = ['title']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'check_in_time', 'check_out_time', 'status']
    list_filter = ['date', 'status']
    search_fields = ['user__full_name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'assigned_to', 'status', 'due_date']
    list_filter = ['status']
    search_fields = ['title', 'assigned_to__full_name']

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'leave_type', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'leave_type']
    search_fields = ['user__full_name']

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'month', 'net_pay', 'status']
    list_filter = ['status', 'month']
    search_fields = ['user__full_name']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message', 'read_status', 'created_at']
    list_filter = ['read_status']
    search_fields = ['user__full_name', 'message']
