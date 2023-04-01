from django.db import models

class Empleados(models.Model):
    Nombre_Empleado = models.CharField(max_length=30)
    Apellido_Empleado = models.CharField(max_length=30)
    Cargo_Empleado = models.CharField(max_length=50)
    Fecha_Ingreso = models.DateField(null=False)


class AreaEmpresa(models.Model):
    Nombre_Area = models.CharField(max_length=30)
    Cantidad_Trabajadores = models.PositiveIntegerField(default=False)

class Sucursal(models.Model):
    Ciudad = models.CharField(max_length=30)
    Numero_Sucursal = models.PositiveIntegerField(default=False)
