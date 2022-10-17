from django.shortcuts import  redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

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
             
            return HttpResponse("Login Invalido")
            
            # Return an 'invalid login' error message.
            
    return render (request, 'login/login.html')