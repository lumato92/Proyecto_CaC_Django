from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

VAT_CONDITION = (
    ('M','MONOTRIBUTO'),
     ('E','EXENTO'),
     ('RI','RESPONSABLE INSCRIPTO'),
     ('NA','NA')
)

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    
    


class Supplier(models.Model):
    
    
    name = models.CharField(max_length = 30)
    tax_id_number = models.IntegerField(null = True, blank= True)
    vat_condition = models.CharField(max_length=30,choices = VAT_CONDITION)
    address = models.CharField(max_length= 30, null= True, blank = True)
    phone = models.IntegerField()
    contact_name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField(null= True, blank =True)
    category = models.ForeignKey(Category, on_delete =models.SET_NULL ,null=True ,blank=True)