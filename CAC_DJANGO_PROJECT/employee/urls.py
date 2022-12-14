from django.urls import path
from . import views


urlpatterns = [
    path('', views.allEmployees, name='allEmployee'),
    path("add/", views.addEmployee, name="addEmployee"),
    path('info/<int:id>', views.infoEmployee, name='infoEmployee'),
    path('edit/<int:id>', views.editEmployee, name='editEmployee'),

    path('change-salary/<int:id>', views.changeSalary, name='changeSalary'),
    path('add-overtime/', views.overTime, name='overTime'),
    path('delete/<int:id>', views.deleteEmployee, name='deleteEmployee'),
    path('send-message/', views.send_message, name='send_message'),
    path('messages/', views.MessagesListView.as_view(), name='messages'),
    # -----URL Managements/Departmens--------#
    path('departments/', views.allDepartments, name='showDepartments'),
    path('departments/<int:id>', views.infoDepartment, name='infoDepartment'),
    path('departments/add', views.addDepartment, name='addDepartment'),
    path('departments/edit/<int:id>', views.editDepartment, name='editDepartment'),
    path('departments/delete/<int:id>', views.deleteDepartment, name='deleteDepartment'),
    # -----URL Puestos--------#
    path('puestos/', views.allPuestos, name='showPuestos'),
    path('puestos/<int:id>', views.infoPuesto, name='infoPuesto'),
    path('puestos/add', views.addPuesto, name='addPuesto'),
    path('puestos/edit/<int:id>', views.editPuesto, name='editPuesto'),
    path('puestos/delete/<int:id>', views.deletePuesto, name='deletePuesto'),
]
