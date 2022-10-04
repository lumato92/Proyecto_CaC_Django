from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.addVendor,name='addVendor'),
    path('all/',views.allVendor, name='allVendor'),
    path('info/<int:id>',views.infoVendor,name='infoVendor'),
    path('edit/<int:id>',views.editVendor, name='editVendor')
]
