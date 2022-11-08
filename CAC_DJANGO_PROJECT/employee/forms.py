from django import forms
from .models import Employee, Department, OverTime, Message, Puesto, Wage, OverTime

GENRE = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )


class EmployeeForm(forms.ModelForm):
    avatar = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['genre'].widget = forms.Select(attrs={'class': 'form-control'}, choices=GENRE)
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control'})
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['id_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['tax_id_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['phone'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['position'] = forms.ModelChoiceField(queryset=Puesto.objects.all(),
                                                         widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        self.fields['is_active'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input  justify-content-center'})
        self.fields['management'] = forms.ModelChoiceField(queryset=Department.objects.all(),
                                                           widget=forms.Select(attrs={'class': 'form-control'}))
        
        # Se coloca position 2 por que es la id de supervisor en la tabla puestos
        self.fields['manager'] = forms.ModelChoiceField(queryset=Employee.objects.all().filter(position = '2'),
                                                        widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['salary'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['avatar'].required = False

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'dob', 'genre', 'id_number', 'tax_id_number', 'email',
                  'address', 'phone', 'start_date', 'position', 'management', 'manager', 'salary',
                  'is_active', 'avatar')

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'genre': 'Sexo',
            'dob': 'Fecha de Nacimiento',
            'tax_id_number': 'Cuil',
            'id_number': 'DNI',
            'email': 'Correo Electronico',
            'address': 'Direccion',
            'phone': 'Telefono',
            'start_date': 'Fecha Contratacion',
            'position': 'Cargo',
            'management': 'Gerencia',
            'manager': 'Jefe',
            'salary': 'Salario',
            'is_active': 'Activo',
            'avatar': 'Imagen'
        }


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['description'].widget = forms.TextInput(attrs={'class': 'form-control'})

    class Meta:
        model = Department
        fields = ('name', 'description')

        labels = {
            'name': 'Nombre',
            'description': 'Description'
        }


class PuestoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PuestoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['description'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['base_salary'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['department'] = forms.ModelChoiceField(queryset=Department.objects.all(),
                                                           widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Puesto
        fields = ('name', 'department', 'description', 'base_salary')

        labels = {
            'name': 'Nombre',
            'department': 'Department',
            'description': 'Description',
            'base_salary': 'base_salary',
        }

class OverTimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OverTimeForm, self).__init__(*args, **kwargs)
        self.fields['employee_id'].widget = forms.NumberInput(attrs={'class':'form-control'})
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        self.fields['amount'].widget = forms.NumberInput(attrs={'class':'form-control','min': '0', 'max':'8', 'step':'0.5'})

        class Meta:
            model = OverTime
            fields = ('employee_id', 'date', 'amount')
            

            labe

class MessageForm(forms.ModelForm):
    receiver = forms.Select()

    class Meta:
        model = Message

        fields = ['receiver', 'msg_content']

        labels = {'receiver': 'Destinatario', 'msg_content': 'Mensaje'}

        widgets = {
            'receiver': forms.Select(
                attrs={
                    'class': "form-control mb-3"
                }
            ),
            'msg_content': forms.Textarea(
                attrs={
                    'class': "form-control mb-3",
                    'rows': 3
                }
            )
        }
        
class WageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(WageForm,self).__init__(*args,**kwargs)
        self.fields['salary'].widget = forms.NumberInput(attrs={'class' : 'form-control'})
        self.fields['salary'].label = 'Nuevo Salario'
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['revision_date'].widget = forms.DateInput(attrs={'type': 'date'})
        
    class Meta:
        model = Wage
        fields = ['salary','date','revision_date']    


class OverTimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OverTimeForm, self).__init__(*args, **kwargs)  
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['amount'].widget=forms.NumberInput(attrs={'step': 0.5})
    
    
    class Meta:
        model = OverTime
        fields = ['date','amount']
        labels = {'date' : 'Fecha', 'amount' : 'Cantidad' }
    