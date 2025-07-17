from django.contrib import admin
from .models import (
    Roles, Users, Departments, Attendance, Tasks,
    Leaves, Payroll, Announcements, Documents, Notifications
)


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name', 'description']
    search_fields = ['role_name']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'role', 'status', 'date_joined']
    list_filter = ['role', 'status']
    search_fields = ['full_name', 'email']


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'check_in_time', 'check_out_time', 'status']
    list_filter = ['date', 'status']
    search_fields = ['user__full_name']


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'assigned_to', 'assigned_by', 'status', 'due_date']
    list_filter = ['status', 'due_date']
    search_fields = ['title', 'assigned_to__full_name', 'assigned_by__full_name']


@admin.register(Leaves)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_date', 'end_date', 'leave_type', 'status']
    list_filter = ['leave_type', 'status']
    search_fields = ['user__full_name']


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'month', 'net_pay', 'status', 'paid_on']
    list_filter = ['month', 'status']
    search_fields = ['user__full_name']


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'created_at']
    search_fields = ['title']


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'doc_type', 'user', 'uploaded_at']
    search_fields = ['doc_type', 'user__full_name']


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'read_status', 'created_at']
    list_filter = ['read_status']
    search_fields = ['user__full_name', 'message']
