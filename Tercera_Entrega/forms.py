from django import forms


class BuscarEmpleadosForm(forms.Form):
    criterio_Nombre = forms.CharField(max_length=30)