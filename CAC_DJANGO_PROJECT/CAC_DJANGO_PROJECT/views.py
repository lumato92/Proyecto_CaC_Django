from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request,'home.html')

def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'home.html')
    else:
        return redirect('loginUser')