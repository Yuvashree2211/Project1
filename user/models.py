from django.db import models

class Roles(models.Model):
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role_name


class Users(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Departments(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Attendance(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.full_name} - {self.date}"



class Tasks(models.Model):
    assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Leaves(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.status}"


class Payroll(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    paid_on = models.DateField()

    def __str__(self):
        return f"{self.user.full_name} - {self.month}"


class Announcements(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Documents(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doc_type} - {self.user.full_name}"


class Notifications(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.user.full_name}"
