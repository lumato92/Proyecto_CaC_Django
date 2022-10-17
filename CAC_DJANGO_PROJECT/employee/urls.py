from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='employee_index'),
    path("add/", views.addEmployee, name="addEmployee"),
    path('all/', views.allEmployees, name='allEmployee'),
    path('info/<int:id>', views.infoEmployee, name='infoEmployee'),
    path('edit/<int:id>', views.editEmployee, name='editEmployee'),
    path('management/',views.addManagement, name='addManagement'),
    path('delete/<int:id>', views.deleteEmployee, name='deleteEmployee'),
    #-----URL Department--------#
    path("departamento/add/", views.addDepartment, name="addDepartment"),
    path('departamentos/all/', views.allDepartments, name='allDepartment'),
    path('departamento/info/<int:id>', views.infoDepartment, name='infoDepartment'),
    path('departamento/edit/<int:id>', views.editDepartment, name='editDepartment'),
    path('departamento/delete/<int:id>', views.deleteDepartment, name='deleteDepartment'),
]
