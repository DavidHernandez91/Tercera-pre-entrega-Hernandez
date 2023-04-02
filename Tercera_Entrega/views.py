from django.shortcuts import render
from django.views.generic import ListView, CreateView
from Tercera_Entrega.models import Empleados, AreaEmpresa, Sucursal
from django.urls import reverse_lazy
from Tercera_Entrega.forms import BuscarEmpleadosForm

def index(request):
    return render(request,"Tercera_Entrega/index.html")

class EmpleadosList(ListView):
    model = Empleados

class AreaEmpresaList(ListView):
    model = AreaEmpresa

class SucursalList(ListView):
    model = Sucursal

class EmpleadosCreate(CreateView):
    model = Empleados
    success_url = reverse_lazy("empleados-create")
    fields = '__all__'

class AreaEmpresaCreate(CreateView):
    model = AreaEmpresa
    success_url = reverse_lazy("areaempresa-create")
    fields = '__all__'

class SucursalCreate(CreateView):
    model = Sucursal
    success_url = reverse_lazy("sucursal-create")
    fields = '__all__'

class BuscarEmpleados(ListView):
    model = Empleados
    context_object_name = 'empleados'

    def get_query(self):
        f = BuscarEmpleadosForm(self.request.GET)
        if f.is_valid():
            return empleados.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Empleados.objects.none()