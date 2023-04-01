from django.db import models

class Empleados(models.Model):
    Nombre_Empleado = models.CharField(max_length=30)
    Apellido_Empleado = models.CharField(max_length=30)
    Cargo_Empleado = models.CharField(max_length=50)
    Fecha_Ingreso = models.DateField(null=False)

    def __str__(self):
        return f"{self.id} - {self.Nombre_Empleado} - {self.Apellido_Empleado}"


class AreaEmpresa(models.Model):
    Nombre_Area = models.CharField(max_length=30)
    Cantidad_Trabajadores = models.PositiveIntegerField(default=False)

    def __str__(self):
        return f"{self.id} - {self.Nombre_Area} - Cantidad de Trabajadores: {self.Cantidad_Trabajadores}"

class Sucursal(models.Model):
    Ciudad = models.CharField(max_length=30)
    Numero_Sucursal = models.PositiveIntegerField(default=False)

    def __str__(self):
        return f"{self.id} - {self.Ciudad} - Numero de Sucursal: {self.Numero_Sucursal}"
