from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from employee.models import Department, Employee, Message
from vendor.models import Category, Supplier


@login_required
def index(request):

    return render(request, 'home.html')


@login_required
def home(request):
    # Agregar Categorías de Proveedores si no existen
    if Category.objects.count() == 0:
        Category.objects.create(name="Comercial", description='')
        Category.objects.create(name="Producción", description='')
        Category.objects.create(name="Financiero", description='')

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        employees = Employee.objects.count()
        suppliers = Supplier.objects.count()
        departments = Department.objects.count()
        employee = {}

        employee_qs = Employee.objects.filter(username=request.user)
        if employee_qs:
            employee = employee_qs.first()

        all_messages = Message.objects.filter(receiver=request.user)
        unread_messages = all_messages.filter(read=False)

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'employees': employees,
            'suppliers': suppliers,
            'employee': employee,
            'departments': departments,
            'unread_messages': unread_messages,
            'all_messages': all_messages.count()
        }

        return render(request, 'home.html', context)
    else:
        return redirect('loginUser')


# PAGE 404 ERROR

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
