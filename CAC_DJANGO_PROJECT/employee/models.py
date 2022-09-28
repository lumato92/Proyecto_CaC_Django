from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

#Gerencias
class Management(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.TextField()
    
    
    




#PUESTOS

class Puesto(models.Model):
    
    name = models.CharField(max_length=30)
    management = models.ForeignKey(Management, on_delete =models.CASCADE)
    description = models.TextField()
    base_salary = models.IntegerField()
    
    
    
    




# Empleado

class Employee(models.Model):
    GENRE = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField(auto_now = True, help_text = "AAAA-MM-DD")
    genre = models.CharField(max_length=20, choices = GENRE)
    cuil = models.IntegerField(null = False)
    dni = models.IntegerField(null = False)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    start_date = models.DateTimeField(auto_now=True, help_text = "AAAA-MM-DD")
    position = models.ForeignKey(Puesto, on_delete = models.CASCADE)
    management = models.ForeignKey(Management, on_delete = models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.DO_NOTHING)
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


    
    
    

    