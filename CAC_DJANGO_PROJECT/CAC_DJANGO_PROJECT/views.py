from django.shortcuts import redirect, render
from django.contrib.auth import authenticate



from django.shortcuts import render

from employee.models import Employee
from vendor.models import Supplier
# Create your views here.


def index(request):
    
    return render(request,'home.html')

def home(request):
    
    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        employees = Employee.objects.count()
        suppliers = Supplier.objects.count()
        
        context = {
            'first_name' : first_name,
            'last_name'  : last_name,
            'employees': employees,
            'suppliers': suppliers
        }
        
        return render(request,'home.html', context)
    else:
        return redirect('loginUser')
    return render(request, 'sidebar2.html')


