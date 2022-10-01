from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
# Create your views here.

def index(request):
    
    return HttpResponse("Pagina empleados")
    
def addEmployee(request):
    
    form = EmployeeForm()
    
    context = {'form':form}
    
    return render(request,'employee/add2.html',context)