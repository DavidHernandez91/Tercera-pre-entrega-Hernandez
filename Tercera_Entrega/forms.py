from django import forms

class SucursalForm(forms.Form):
   Ciudad = forms.CharField(max_length=30)
   


class BuscarSucursalForm(forms.Form):
    criterio__ciudad = forms.CharField(max_length=30)