from django import forms

class FormCargo(forms.Form):
    nome = forms.CharField(max_length = 50)