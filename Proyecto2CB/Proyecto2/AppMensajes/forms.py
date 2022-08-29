from django import forms

class MensajeFormulario(forms.Form):
    cuerpo= forms.CharField(max_length=10000)
