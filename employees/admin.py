from django.contrib import admin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'second_name',
        'role',
        'level')