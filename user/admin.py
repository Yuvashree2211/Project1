from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Salary)
admin.site.register(Holiday)
admin.site.register(Timesheet)
admin.site.register(Leave)
