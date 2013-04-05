from django import forms


class FormCargo(forms.Form):
    nome = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {'placeholder': 'Cargo'}))    
    #nome = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {'class': 'datepicker', 'data-date': '12-02-2012', 'data-date-format' : 'dd-mm-yyyy', 'value':'12-02-2012'}))
    
    