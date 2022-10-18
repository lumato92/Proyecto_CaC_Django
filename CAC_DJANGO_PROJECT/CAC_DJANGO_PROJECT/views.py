from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse

from django.db.models import Sum

from employee.models import Employee
from vendor.models import Supplier
# Create your views here.

def index(request):
    
    return render(request,'home.html')

def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        
        context = {
            'first_name' : first_name,
            'last_name'  : last_name
        }
        
        return render(request,'home.html', context)
    else:
        return redirect('loginUser')