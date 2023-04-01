from django import forms

class PersonaForm(forms.Form):
    Nombre_Empleado = models.CharField(max_length=30)
    Apellido_Empleado = models.CharField(max_length=30)
    Cargo_Empleado = models.CharField(max_length=50)
    Fecha_Ingreso = models.DateField(null=False)

class AreaEmpresaForm(forms.Form):
    Nombre_Area = models.CharField(max_length=30)
    Cantidad_Trabajadores = models.PositiveIntegerField(default=False)

class SucursalForm(forms.Form):
    Ciudad = models.CharField(max_length=30)
    Numero_Sucursal = models.PositiveIntegerField(default=False)

class BuscarEmpleadosForm(forms.Form):
    criterio_Nombre = forms.CharField(max_length=30)