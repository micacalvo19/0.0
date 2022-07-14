from django import forms

class SocioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_de_socio = forms.IntegerField()

class PersonalForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    cargo = forms.CharField(max_length=50)

class ActividadForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad_de_personas = forms.IntegerField()

