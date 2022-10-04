from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='employee_index'),
    path("add/",views.addEmployee, name="addEmployee"),
    path('all/',views.allEmployees,name='allEmployee'),
    path('info/<int:id>',views.infoEmployee,name='infoEmployee'),
    path('edit/<int:id>',views.editEmployee,name='editEmployee')
    
]
