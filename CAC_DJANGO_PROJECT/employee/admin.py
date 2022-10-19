from django.contrib import admin

from .models import Employee, Department, Puesto


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Puesto)
