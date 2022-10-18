from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Sum

from employee.models import Employee
from vendor.models import Supplier
# Create your views here.

def index(request):
    
    return render(request,'sidebar2.html')

def home(request):
#    return render(request,'home.html')
    employees = Employee.objects.count()
    suppliers = Supplier.objects.count()
    
    context = { 'employees' : employees, 'suppliers' : suppliers}    

    return render(request,'home.html', context)
    