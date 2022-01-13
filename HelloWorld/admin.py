# Register your models here.

from django.contrib import admin
from HelloWorld.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ['empNo', 'empName', 'empSalary', 'empAddress']


admin.site.register(Employee)
