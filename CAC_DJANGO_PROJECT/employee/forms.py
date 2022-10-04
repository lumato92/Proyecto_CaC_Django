
from django import forms
from .models import Employee, Department, Puesto
from .widget import DatePickerInput
from django.forms.widgets import SelectDateWidget

GENRE = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )
    
    

class EmployeeForm(forms.ModelForm):
    
   
    
    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control'})
        # self.fields['genre'].widget = forms.ChoiceField(attrs={'class':'form-control'})
        self.fields['dob'].widget = forms.DateInput(attrs={'type':'date','class':'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'type':'email','class':'form-control'})
        self.fields['start_date'].widget = forms.DateInput(attrs={'type':'date'})
        self.fields['id_number'].widget = forms.NumberInput(attrs={'class':'form-control'})
        self.fields['tax_id_number'].widget = forms.NumberInput(attrs={'class':'form-control'})
        self.fields['address'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['phone'].widget = forms.NumberInput(attrs={'class':'form-control'})

        self.fields['start_date'].widget = forms.DateInput(attrs={'type':'date','class':'form-control'})
        self.fields['is_active'].widget = forms.CheckboxInput()
    
    
    
    class Meta:
        model = Employee
        
        fields = ('first_name','last_name','dob','genre','id_number','tax_id_number','email',
                  'address','phone','start_date','position','management','manager','salary','is_active')
        

        labels = {
            'first_name':'Nombre',
            'last_name' : 'Apellido',
            'genre': 'Sexo',
            'dob' : 'Fecha de Nacimiento',
            'tax_id_number' : 'Cuil',
            'id_number' : 'DNI',
            'email' : 'Correo Electronico',
            'address' : 'Direccion',
            'phone' : 'Telefono',
            'start_date' : 'Fecha Contratacion',
            'position' : 'Cargo',
            'management' : 'Gerencia',
            'manager' : 'Jefe',
            'salary'   : 'Salario',
            'is_active' : 'Activo'
        }


