from unicodedata import name
from django.contrib.auth.models import User , Group
import random
from employee.models import Employee


DEFAULT_PASSWORD = 'ADMIN123!'

def newUser (name,lastname, email, position):
    
    """Genero un nuevo usuario apartir de un nuevo empleado,tienen una password default 
    """
    
    
    try:
        # Defino el username utilizando el nombre y apellido con el formato 
        # primera letra del nombre + apellido + random de 1 a 10
        username = f'{name[:1]}{lastname.lower()}{random.randint(0,10)}'
        
        user = User.objects.create_user(username,email,DEFAULT_PASSWORD)
        
        user.first_name = name
        user.last_name = lastname
        user.save()
        
        # Modifico el ultimo empleado agregado y le asigno al username el user creado para enlazar la tabla 
        # Employee y User
        obj = Employee.objects.latest('id')
        obj.username=user
        obj.save()
        
        if position != 'Supervisor':
            
            addEmployeeGroup(user)
            
    
    except:
        
        return False

    
    
def addEmployeeGroup(user):
    
    employeeGroup = Group.objects.get(name = 'employee')
    employeeGroup.user_set.add(user)
    
    return
    
    