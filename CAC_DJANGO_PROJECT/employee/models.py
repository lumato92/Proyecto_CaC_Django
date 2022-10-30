from django.contrib.auth.models import User
from django.db import models

from PIL import Image


# Gerencias
class Department(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Departamento"


# PUESTOS
class Puesto(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    base_salary = models.FloatField()

    def __str__(self):
        return self.name


# Empleado
class Employee(models.Model):
    GENRE = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE, default='FEMENINO')
    id_number = models.IntegerField(null=False)
    tax_id_number = models.IntegerField(null=False)
    address = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30, default="Argentina")
    email = models.EmailField()
    phone = models.IntegerField()
    start_date = models.DateField()
    position = models.ForeignKey(Puesto, on_delete=models.CASCADE, blank=True, null=True)
    management = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    salary = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(default='img/no-image.png', upload_to='profile_images')

    class Meta:
        verbose_name = "Empleado"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
