
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('empleados/', include("employee.urls")),
    path('proveedores/', include('vendor.urls')),
    path('home/', views.home, name='home'),
    path('auth0/',include('auth0.urls'))
]
