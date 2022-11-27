
from django import forms
from .models import Category, Supplier, VAT_CONDITION


class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['tax_id_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': '4', 'cols': '150'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['phone'].widget = forms.NumberInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['contact_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['vat_condition'].widget = forms.Select(attrs={'class': 'form-control'}, choices=VAT_CONDITION)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all(),
                                                         widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Supplier
        fields = ('name', 'tax_id_number', 'vat_condition',
                  'category', 'description', 'address', 'phone', 'email',
                  'contact_name')
        labels = {
            'name': 'Proveedor',
            'tax_id_number': 'CUIT',
            'vat_condition': 'Condicion IVA',
            'category': 'Categoria',
            'description': 'Descripcion',
            'address': 'direccion',
            'phone': 'Telefono',
            'email': 'Correo Electronico',
            'contact_name': 'Persona de Contacto',
        }
