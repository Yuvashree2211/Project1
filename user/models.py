from django.db import models

class Role(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    permissions_summary = models.CharField(max_length=255)  # renamed

class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_permissions')
    title = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    description = models.TextField()


class User(models.Model):
    role = models.CharField(max_length=100)  # or ForeignKey to Role
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

class Timesheet(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    project = models.CharField(max_length=100)

class Salary(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Holiday(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=50)
    to = models.CharField(max_length=100)
    from_date = models.CharField(max_length=100)
