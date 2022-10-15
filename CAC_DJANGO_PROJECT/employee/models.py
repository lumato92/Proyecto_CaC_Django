from django.contrib.auth.models import User
from django.db import models
from .misc import COUNTRY_LIST

# Create your models here.

#Gerencias
class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    




#PUESTOS

class Puesto(models.Model):
    
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete =models.CASCADE)
    description = models.TextField()
    base_salary = models.FloatField()
    
    
    def __str__(self):
        return self.name
    
    
    
    
    




# Empleado

class Employee(models.Model):
    GENRE = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )
    
    
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    genre = models.CharField( max_length= 20,choices = GENRE, default='FEMENINO')
    id_number = models.IntegerField(null = False)
    tax_id_number = models.IntegerField(null = False)
    address = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30,default="Argentina")
    email = models.EmailField()
    phone = models.IntegerField()
    start_date = models.DateField()
    position = models.ForeignKey(Puesto, on_delete = models.CASCADE)
    management = models.ForeignKey(Department, on_delete = models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.DO_NOTHING)
    salary = models.FloatField(null = True)
    is_active = models.BooleanField(default=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE,blank = True , null = True)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    
    

    