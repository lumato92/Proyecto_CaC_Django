from random import choices
from django.db import models
from vendor.models import Supplier


# INCOMPLETO

INVOICE_TYPE = (
    ('fact_a','A'),
    ('fact_b', 'B'),
    ('fact_c','C'),
    ('none','NA'),
    ('not_cr','Nota Credito')
)


UTILITIES = 

# Create your models here.
class Purchase(models.Model):
    
    date = models.DateField()
    vendor = models.ForeignKey(Supplier, on_delete = models.DO_NOTHING, blank=True, null= True)
    invoice_type = models.CharField(max_length = 10, choices= INVOICE_TYPE)
    invoice_number = models.IntegerField(blank=True,null=True)
    subtotal = models.FloatField(blank=True, null = True)
    vat_21 =  models.FloatField(blank=True, null = True)
    vat_105 =  models.FloatField(blank=True, null = True)
    bonus =  models.FloatField(blank=True, null = True)
    total =   models.FloatField(blank=True, null = True)
    
class Expense(models.Model):
    
    date = models.DateField()
    

    
    
    
    
    