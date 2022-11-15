from django.contrib import admin

from .models import Employee, Department, Message, Puesto , Wage , OverTime


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Message)
admin.site.register(Puesto)
admin.site.register(Wage)
admin.site.register(OverTime)
