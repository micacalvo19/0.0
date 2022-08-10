from socket import fromshare
from django import forms

class RecetaFormulario(forms.Form):

    #Especificar los campos
    titulo = forms.CharField(max_length=20)
    cuerpo = forms.CharField(max_length=10000)
   # imagen= forms.ImageField(label='imagen')
    fecha= forms.DateField()
