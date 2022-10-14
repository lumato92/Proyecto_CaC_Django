from django.shortcuts import render
from django.http import HttpResponse

from employee.models import Employee
from .forms import EmployeeForm
# Create your views here.

def index(request):
    
    return HttpResponse("Pagina empleados")
    
def addEmployee(request):
    
    edit = False
    
    if (request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            
            form.save()
        
            return HttpResponse("Empleado agregado")
        else:
            print(form.errors.as_data())
            # form = EmployeeForm()
            # context = {'form':form}
            # return render(request,'employee/add2.html',context)
            return HttpResponse("HUBO UN ERROR")
    
    else:       
        form = EmployeeForm()
    
        context = {'form':form,
                   'edit': edit}
    
    return render(request,'employee/addemployee.html',context)


def allEmployees(request):
    
    employees = Employee.objects.all()
    
    context = { 'employees' : employees}    
    return render(request,'employee/allemployee.html', context)


def infoEmployee(request,id):
    employee = Employee.objects.get(id=id)
    
    context = {'employee' : employee}
    
    return render(request,'employee/infoemployee.html',context)





def editEmployee(request,id):
    employee = Employee.objects.get(id=id)
    edit = True
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            
            form.save()
        
            return HttpResponse("Empleado Editado")
        else:
            print(form.errors.as_data())

            return HttpResponse("HUBO UN ERROR")
        
    else:
    
    
        
        employeeform = EmployeeForm(instance = employee)
    
        context = {'form' : employeeform,
                   'edit' : edit}
    
    return render(request,'employee/addemployee.html',context)


def addManagement(request):
    
    # return HttpResponse ("ok")
    return render (request, "base.html")