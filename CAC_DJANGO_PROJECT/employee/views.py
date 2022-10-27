from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from employee.models import Employee, Department, Puesto

from .forms import EmployeeForm,DepartmentForm,PuestoForm


def index(request):
    return HttpResponse("Pagina empleados")

# --------Employee----------------------------
# --------Create------------------------------
def addEmployee(request):
    edit = False
    if (request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado agregado exitosamente!')
            return redirect('allEmployee')
        else:
            print(form.errors.as_data())
            form_errors = form.errors
            messages.error(request, form_errors)
            # form = EmployeeForm()
            # context = {'form':form}
            # return render(request,'employee/add2.html',context)
            # return HttpResponse("HUBO UN ERROR")
            # return redirect(request.META['HTTP_REFERER'])
            return render(request, 'employee/addemployee.html', {'form': form})
    else:
        form = EmployeeForm()
        context = {'form': form,
                   'edit': edit}

    return render(request, 'employee/addemployee.html', context)
# --------Index------------------------------
def allEmployees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee/allemployee.html', context)
# --------Show------------------------------
def infoEmployee(request, id):
    employee = Employee.objects.get(id=id)
    context = {'employee': employee}
    return render(request, 'employee/infoemployee.html', context)
# --------Edit------------------------------
def editEmployee(request, id):
    employee = Employee.objects.get(id=id)
    edit = True
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizo el empleado!')
            return redirect('allEmployee')
        else:
            print(form.errors.as_data())
            messages.warning(request, 'HUBO UN ERROR')
            return redirect('allEmployee')
    else:
        employeeform = EmployeeForm(instance=employee)
        context = {'form': employeeform,
                   'edit': edit}
    return render(request, 'employee/addemployee.html', context)
# --------Destroy------------------------------
def deleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.error(request, 'Document deleted.')
    return redirect('allEmployee')
# --------End Employee------------------------------
#----------------------------------------------------------------------

# --------Show Puestos------------------------------
def showPuestos(request):
    puestos = Puesto.objects.all()
    return render(request, 'employee/showpuestos.html', {'puestos': puestos})

#---------Departments----------------------------------------------------
#--------Index-----------------------------------------------------------
def allDepartments(request):
    departments = Department.objects.all()
    context = { 'departments' : departments}
    return render(request,'department/alldepartment.html', context)
# --------Show------------------------------
def infoDepartment(request, id):
    department = Department.objects.get(id=id)
    context = {'department': department}
    return render(request, 'department/infodepartment.html', context)
# --------Create----------------------------------------------------------
def addDepartment(request):
    edit = False
    if (request.method == 'POST'):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento creado exitosamente!')
            return redirect('showDepartments')
        else:
            print(form.errors.as_data())
            form_errors = form.errors
            messages.error(request, form_errors)
            return render(request, 'department/adddepartment.html', {'form': form})
    else:
        form = DepartmentForm()
        context = {'form': form,
                   'edit': edit}

    return render(request, 'department/adddepartment.html', context)

# --------Edit------------------------------
def editDepartment(request, id):
    department = Department.objects.get(id=id)
    edit = True
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizo el departamento!')
            return redirect('showDepartments')
        else:
            print(form.errors.as_data())
            messages.warning(request, 'HUBO UN ERROR')
            return redirect('showDepartments')
    else:
        departmentform = DepartmentForm(instance=department)
        context = {'form': departmentform,
                   'edit': edit}
    return render(request, 'department/adddepartment.html', context)
# --------Destroy------------------------------
def deleteDepartment(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.error(request, 'Document deleted.')
    return redirect('showDepartments')

#---------Departments END---------------------------------------------------

#---------Puestos----------------------------------------------------
#--------Index-----------------------------------------------------------
def allPuestos(request):
    puestos = Puesto.objects.all()
    context = { 'puestos' : puestos}
    return render(request,'puesto/allpuestos.html', context)
# --------Show------------------------------
def infoPuesto(request, id):
    puesto = Puesto.objects.get(id=id)
    context = {'puesto': puesto}
    return render(request, 'puesto/infopuesto.html', context)
# --------Create----------------------------------------------------------
def addPuesto(request):
    edit = False
    if (request.method == 'POST'):
        form = PuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Puesto creado exitosamente!')
            return redirect('showPuestos')
        else:
            print(form.errors.as_data())
            form_errors = form.errors
            messages.error(request, form_errors)
            return render(request, 'puesto/addpuesto.html', {'form': form})
    else:
        form = PuestoForm()
        context = {'form': form,
                   'edit': edit}

    return render(request, 'puesto/addpuesto.html', context)

# --------Edit------------------------------
def editPuesto(request, id):
    puesto = Puesto.objects.get(id=id)
    edit = True
    if request.method == 'POST':
        form = PuestoForm(request.POST, instance=puesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se actualizo el puesto!')
            return redirect('showPuestos')
        else:
            print(form.errors.as_data())
            messages.warning(request, 'HUBO UN ERROR')
            return redirect('showPuestos')
    else:
        puestoform = PuestoForm(instance=puesto)
        context = {'form': puestoform,
                   'edit': edit}
    return render(request, 'puesto/addpuesto.html', context)
# --------Destroy------------------------------
def deletePuesto(request, id):
    puesto = Puesto.objects.get(id=id)
    puesto.delete()
    messages.error(request, 'Puesto borrado con exito.')
    return redirect('showPuestos')

#---------Departments END---------------------------------------------------
