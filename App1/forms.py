from django import forms

class FormularioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_de_socio = forms.IntegerField()