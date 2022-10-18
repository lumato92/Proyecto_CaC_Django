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
    #-----URL Managements--------#
    path('managements/',views.showManagements, name='showManagements'),
    #-----URL Puestos--------#
    path('puestos/',views.showPuestos, name='showPuestos'),
    
]
