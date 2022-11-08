from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Cambio la funcion __str__ default del model User 
def full_name(self):
    return f'{self.first_name} {self.last_name} ({self.username})'

User.add_to_class("__str__", full_name)