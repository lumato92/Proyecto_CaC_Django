from django.db import models

VAT_CONDITION = (
    ('M', 'MONOTRIBUTO'),
    ('E', 'EXENTO'),
    ('RI', 'RESPONSABLE INSCRIPTO'),
    ('NA', 'NA')
)


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    tax_id_number = models.IntegerField(null=True, blank=True)
    vat_condition = models.CharField(max_length=30, choices=VAT_CONDITION)
    address = models.CharField(max_length=30, null=True, blank=True)
    phone = models.IntegerField()
    contact_name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Proveedor"
