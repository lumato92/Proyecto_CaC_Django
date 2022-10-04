from django.shortcuts import render,redirect
from django.http import HttpResponse
import vendor

from vendor.models import Supplier
from .forms import SupplierForm

# Create your views here.

def addVendor(request):

    edit = False
    
    if (request.method == 'POST'):
        form = SupplierForm(request.POST)
        if form.is_valid():
            
            form.save()
        
            return redirect('index')
        else:
            print(form.errors.as_data())

            return HttpResponse("HUBO UN ERROR")
    
    else:       
        form = SupplierForm()
    
        context = {'form':form,
                   'edit': edit}
    
    # return HttpResponse(" AGREGAR PROVEEDOR")
    return render (request ,'vendor/addvendor.html',context)

def allVendor(request):
    
    vendors = Supplier.objects.all()
    
    context = { 'vendors' : vendors}
    
    
    return render(request,'vendor/allvendor.html',context)


def infoVendor(request,id):

    return 
    
def editVendor(request,id):
    vendor = Supplier.objects.get(id=id)
    edit = True
    
    if request.method == 'POST':
        form = SupplierForm(request.POST,instance=vendor)
        if form.is_valid():
            
            form.save()
        
            return HttpResponse("Proveedor Editado")
        else:
            print(form.errors.as_data())

            return HttpResponse("HUBO UN ERROR")
        
    else:
    
    
        
        form = SupplierForm(instance = vendor)
    
        context = {'form' : form,
                   'edit' : edit}
    
    return render(request,'vendor/addvendor.html',context)