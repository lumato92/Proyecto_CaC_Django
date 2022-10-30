from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from employee.models import Employee
from vendor.models import Supplier
# Create your views here.


@login_required
def index(request):

    return render(request, 'home.html')


@login_required
def home(request):

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        employees = Employee.objects.count()
        suppliers = Supplier.objects.count()
        employee = {}

        employee_qs = Employee.objects.filter(username=request.user)
        if employee_qs:
            employee = employee_qs.first()

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'employees': employees,
            'suppliers': suppliers,
            'employee': employee,
        }

        return render(request, 'home.html', context)
    else:
        return redirect('loginUser')
    

# PAGE 404 ERROR 

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)