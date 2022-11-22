from django.shortcuts import  redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from employee.models import Employee ,OverTime , Wage
# Create your views here.
def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # return render(request,'base.html')
            return redirect('home')
            # return HttpResponse (f"Login valido {username}")
            
        else:
            messages.error(request, 'Contraseña o Usuario Invalido')
            redirect ('loginUser')
            
            # Return an 'invalid login' error message.
            
    return render (request, 'login/login.html')


def logoutUser(request):
    logout(request)
    
    return render(request, 'users/logout.html')


def userProfile(request, username):
    user = User.objects.get(username=username)
    employee = Employee.objects.get(pk =request.user.id)
    overtime = OverTime.objects.filter(employee_id_id = employee)
    print(employee)
    context = {'user' : user,
                'employee' :employee,
                'overtimeList':overtime
            }
    return render(request, 'users/account_profile.html', context)
