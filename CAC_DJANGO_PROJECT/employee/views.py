from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from employee.models import Employee,Department, Puesto

from .forms import EmployeeForm, DepartmentForm, PuestoForm
# Create your views here.

def index(request):
    return HttpResponse("Pagina empleados")
#--------Employee----------------------------#    
#--------Create------------------------------#    
def addEmployee(request):
    edit = False
    if (request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Empleado agregado")
            messages.success(request, 'Empleado agregado exitosamente!')
            return redirect('allEmployee')  
        else:
            print(form.errors.as_data())
            form_errors = form.errors
            messages.error(request, form_errors )
            # form = EmployeeForm()
            # context = {'form':form}
            # return render(request,'employee/add2.html',context)
            #return HttpResponse("HUBO UN ERROR")
            #return redirect(request.META['HTTP_REFERER']) 
            return render(request, 'employee/addemployee.html', { 'form': form })
    else:       
        form = EmployeeForm()
        context = {'form':form,
                   'edit': edit}
    return render(request,'employee/addemployee.html',context)

#--------Index------------------------------#    
def allEmployees(request):
    employees = Employee.objects.all()
    context = { 'employees' : employees}    
    return render(request,'employee/allemployee.html', context)
#--------Show------------------------------#    
def infoEmployee(request,id):
    employee = Employee.objects.get(id=id)
    context = {'employee' : employee}
    return render(request,'employee/infoemployee.html',context)
#--------Edit------------------------------#    
def editEmployee(request,id):
    employee = Employee.objects.get(id=id)
    edit = True    
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizo el empleado!')
            return redirect('allEmployee')  
        else:
            print(form.errors.as_data())
            #return HttpResponse("HUBO UN ERROR")
            messages.warning(request, 'HUBO UN ERROR')
            return redirect('allEmployee')  
    else:
        employeeform = EmployeeForm(instance = employee)
        context = {'form' : employeeform,
                   'edit' : edit}
    return render(request,'employee/addemployee.html',context)
#--------Destroy------------------------------#    
def deleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.error(request, 'Document deleted.')
    return redirect('allEmployee')  
#--------End Employee------------------------------#    

def addManagement(request):    
    # return HttpResponse ("ok")
    
    return render (request, "base.html")

#--------Department--------------------------#    
#--------Create------------------------------#    
def addDepartment(request):
    edit = False
    if (request.method == 'POST'):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Empleado agregado")
            messages.success(request, 'Departamento creado exitosamente!')
            return redirect('allDepartment')  
        else:
            form_errors = form.errors
            messages.error(request, form_errors )
            return render(request, 'department/adddepartment.html', { 'form': form })
    else:       
        form = DepartmentForm()
        context = {'form':form,
                   'edit': edit}
    return render(request,'department/adddepartment.html',context)

#--------Index------------------------------#    
def allDepartments(request):
    departments = Department.objects.all()
    context = { 'departments' : departments}    
    return render(request,'department/alldepartment.html', context)
#--------Show------------------------------#    
def infoDepartment(request,id):
    department = Department.objects.get(id=id)
    context = {'department' : department}
    return render(request,'department/infodepartment.html',context)
#--------Edit------------------------------#    
def editDepartment(request,id):
    department = Department.objects.get(id=id)
    edit = True    
    if request.method == 'POST':
        form = DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizo el departmanto!')
            return redirect('allDepartment')  
        else:
            print(form.errors.as_data())
            #return HttpResponse("HUBO UN ERROR")
            messages.warning(request, 'HUBO UN ERROR')
            return redirect('allDepartment')  
    else:
        departmentform = DepartmentForm(instance = department)
        context = {'form' : departmentform,
                   'edit' : edit}
    return render(request,'department/adddepartment.html',context)
#--------Destroy------------------------------#    
def deleteDepartment(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.error(request, 'Department deleted.')
    return redirect('allDepartment')  
#--------End Employee------------------------------#    