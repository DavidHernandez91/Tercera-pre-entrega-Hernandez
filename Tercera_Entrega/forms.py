from django import forms

class SucursalForm(forms.Form):
   Ciudad = forms.CharField(max_length=30)
   


class BuscarSucursalesForm(forms.Form):
    criterio__Ciudad = forms.CharField(max_length=30)