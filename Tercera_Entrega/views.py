from django.shortcuts import render
from django.views.generic import ListView, CreateView

class EmpleadosList(ListView):
    model = Empleados

class AreaEmpresaList(ListView):
    model = AreaEmpresa

class SucursalList(ListView):
    model = Sucursal

class EmpleadosCreate(CreateView):
    model = Empleados
    fields = '__all__'

class AreaEmpresaCreate(CreateView):
    model = AreaEmpresa
    fields = '__all__'

class SucursalCreate(CreateView):
    model = Empleados
    fields = '__all__'
