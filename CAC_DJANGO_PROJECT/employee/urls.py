from django.urls import path
from . import views


urlpatterns = [
    path('', views.allEmployees, name='allEmployee'),
    path("add/", views.addEmployee, name="addEmployee"),
    path('info/<int:id>', views.infoEmployee, name='infoEmployee'),
    path('edit/<int:id>', views.editEmployee, name='editEmployee'),
    # path('management/', views.addManagement, name='addManagement'),
    path('delete/<int:id>', views.deleteEmployee, name='deleteEmployee'),
    path('inbox/', views.MessageListView.as_view(), name='inbox'),
    path('send-message/', views.send_message, name='send_message'),
    path('sent-messages/', views.SentMessagesListView.as_view(), name='sent_messages'),
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
