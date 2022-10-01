from email.policy import default
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from .misc import COUNTRY_LIST

# Create your models here.

#Gerencias
class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.TextField()
    
    
    
    




#PUESTOS

class Puesto(models.Model):
    
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete =models.CASCADE)
    description = models.TextField()
    base_salary = models.FloatField()
    
    
    
    




# Empleado

class Employee(models.Model):
    GENRE = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )
    
    
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    genre = models.CharField( max_length= 20,choices = GENRE, default='FEMENINO')
    id_number = models.IntegerField(null = False)
    tax_id_number = models.IntegerField(null = False)
    address = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30,default="Argentina")
    email = models.EmailField()
    phone = models.IntegerField()
    start_date = models.DateTimeField()
    position = models.ForeignKey(Puesto, on_delete = models.CASCADE)
    management = models.ForeignKey(Department, on_delete = models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.DO_NOTHING)
    salary = models.FloatField(null = True)
    is_active = models.BooleanField()
    
    # class Meta:
        
    #     name = Employee
        
    #     fields = ('first_name','last_name','dob','gender','cuil','dni','email',
    #               'address','phone','position','management','manager','is_active')
        
    #     labels = {
    #         'first_name':'Nombre',
    #         'last_name' : 'Apellido',
    #         'dob' : 'Fecha de Nacimiento',
    #         'gender': 'Sexo',
    #         'cuil' : 'Cuil',
    #         'dni' : 'DNI',
    #         'email' : 'Correo Electronico',
    #         'address' : 'Direccion',
    #         'phone' : 'Telefono',
    #         'position' : 'Cargo',
    #         'management' : 'Gerencia',
    #         'manager' : 'Jefe',
    #         'is_active' : 'Activo'
    #     }


    
    
    

    