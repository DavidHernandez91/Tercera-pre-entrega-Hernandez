from django.shortcuts import render
from django.views.generic import ListView, CreateView
from Tercera_Entrega.models import Empleados, AreaEmpresa, Sucursal
from django.urls import reverse_lazy


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

def buscar_sucursal(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        resultados = Sucursal.objects.filter(Ciudad=query)
        return render(request,'Tercera_Entrega/resultados_busqueda.html', {'resultados': resultados})
    return render(request,'Tercera_Entrega/formulario_busqueda.html')
    
    

   