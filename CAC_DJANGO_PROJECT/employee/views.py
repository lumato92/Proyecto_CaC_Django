from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from employee.forms import EmployeeForm, DepartmentForm, MessageForm, PuestoForm ,WageForm, OverTimeForm
from employee.models import Employee, Department, Message, Puesto, Wage ,OverTime
from login.user import newUser


def index(request):
    return HttpResponse("Pagina empleados")


# --------Employee----------------------------
# --------Create------------------------------
@login_required
def addEmployee(request):
    edit = False
    if (request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            position = form.cleaned_data.get('position')
            print(position)

            if newUser(name, lastName, email, position):
                print("USER CREADO")
            else:
                print("error")
            # return HttpResponse("Empleado agregado")
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
@login_required
def allEmployees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee/allemployee.html', context)


# --------Show------------------------------
@login_required
def infoEmployee(request, id):
    employee = Employee.objects.get(id=id)
    context = {'employee': employee}
    return render(request, 'employee/infoemployee.html', context)


# --------Edit------------------------------
@login_required
def editEmployee(request, id):
    employee = Employee.objects.get(id=id)
    edit = True
    if request.method == 'POST':
        post_data = request.POST or None
        file_data = request.FILES or None

        form = EmployeeForm(post_data, file_data, instance=employee)
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
                   'edit': edit,
                   'employee': employee}

    return render(request, 'employee/addemployee.html', context)

#------------Salary------------------------------
@login_required
def changeSalary(request,id):
    employee = Employee.objects.get(id=id)
    form = WageForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            
            # Guardo nuevo registro de cambio de salario
        
            instance = form.save(commit=False)
            instance.employee = employee
            instance.save()
            
            # Actualizo el nuevo salario al perfil del empleado
            employee.salary = instance.salary
            employee.save()
            messages.success(request, 'Salario Actualizado ')

            
            return redirect('allEmployee')
        else:
            
            messages.error(request, "ERROR")
            return redirect('allEmployee')
    
    else:
        
        context = {'employee' : employee,
                   'form' : form}
        return render(request, 'employee/changeSalary.html',context)
    
    
# ---------------Horas Extras -----------------------

@login_required
def overTime(request):
    
    
    # Con el id del user busco el empleado
    print(request.user.id)
    employee = Employee.objects.get(pk = request.user.id)
    
    form = OverTimeForm(request.POST or None)
    
    overtimeList = OverTime.objects.filter(employee_id_id = employee)
    print(overtimeList)
    
    if request.method == 'POST':
        if form.is_valid():
            
            # Guardo nuevo registro de cambio de salario
        
            instance = form.save(commit=False)
            instance.employee_id = employee
            instance.save()
            messages.success(request, 'Horas Extras Cargadas ')

            
            return redirect('allEmployee')
        else:
            
            messages.error(request, "ERROR")
            return redirect('allEmployee')
        
    
    else:
        context = {
            'employee': employee,
            'form' : form,
            'overtimeList': overtimeList
        }
        return render(request, 'employee/addOvertime.html', context)


# --------Destroy------------------------------
@login_required
def deleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.error(request, 'Document deleted.')
    return redirect('allEmployee')
# --------End Employee------------------------------


# --------Show Gerencias------------------------------
@login_required
def addManagement(request):
    # return HttpResponse ("ok")
    return render(request, "base.html")


@login_required
def showManagements(request):
    # return HttpResponse ("ok")
    managements = Department.objects.all()
    # return HttpResponse(f"""<h1> Listado de proyectos </h1>""")
    return render(request, 'employee/showmanagements.html', {'managements': managements})


# --------Show Puestos------------------------------
@login_required
def showPuestos(request):
    puestos = Puesto.objects.all()
    return render(request, 'employee/showpuestos.html', {'puestos': puestos})


# ---------Departments----------------------------------------------------
# --------Index-----------------------------------------------------------
@login_required
def allDepartments(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'department/alldepartment.html', context)


# --------Show------------------------------
@login_required
def infoDepartment(request, id):
    department = Department.objects.get(id=id)
    context = {'department': department}
    return render(request, 'department/infodepartment.html', context)


# --------Create----------------------------------------------------------
@login_required
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
@login_required
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
@login_required
def deleteDepartment(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.error(request, 'Document deleted.')
    return redirect('showDepartments')


# ---------Departments END---------------------------------------------------

# ---------Puestos----------------------------------------------------
# --------Index-----------------------------------------------------------
@login_required
def allPuestos(request):
    puestos = Puesto.objects.all()
    context = {'puestos': puestos}
    return render(request, 'puesto/allpuestos.html', context)


# --------Show------------------------------
@login_required
def infoPuesto(request, id):
    puesto = Puesto.objects.get(id=id)
    context = {'puesto': puesto}
    return render(request, 'puesto/infopuesto.html', context)


# --------Create----------------------------------------------------------
@login_required
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
@login_required
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
@login_required
def deletePuesto(request, id):
    puesto = Puesto.objects.get(id=id)
    puesto.delete()
    messages.error(request, 'Puesto borrado con exito.')
    return redirect('showPuestos')

# ---------Departments END---------------------------------------------------


# -------- Messages ------------------------------
class MessageListView(ListView):
    model = Message
    context_object_name = 'message_list'
    template_name = 'employee/inbox.html'

    def get_queryset(self):
        # Aprovecho a marcar todos los mensajes como leidos
        this_qs = Message.objects.filter(receiver=self.request.user)
        this_qs.update(read=True)
        return this_qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bandeja de Entrada'
        return context


class SentMessagesListView(ListView):
    model = Message
    context_object_name = 'message_list'
    template_name = 'employee/inbox.html'

    def get_queryset(self):
        this_qs = Message.objects.filter(sender=self.request.user)
        return this_qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Elementos enviados'
        return context


@login_required
def send_message(request):
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        new_message = form.save(commit=False)

        sender = request.user
        new_message.sender = sender

        new_message.save()

        return redirect('inbox')

    context = {
        'form': form
    }

    return render(request, 'employee/send-message.html', context)
