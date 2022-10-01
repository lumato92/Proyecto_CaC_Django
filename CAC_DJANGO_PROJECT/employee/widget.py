from socket import fromshare
from django import forms

class DatePickerInput(forms.DateInput):
    type = 'date'
    
class TimePickerInput(forms.TimeInput):
    input_type = 'time'
    
class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'