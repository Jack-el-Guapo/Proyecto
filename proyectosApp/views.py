from django.shortcuts import render, redirect
from proyectosApp.forms import FormProyecto
from proyectosApp.models import Proyecto


def listadoProyectos(request):
    proyectos = proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'proyectos.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
            return listadoProyectos(request)
    data = {'form': form}
    return render (request, 'agregarProyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
        form.save()
        return listadoProyectos(request)
    data = {'form': form}
    return render (request, 'agregarProyecto.html', data)

   
    
# Create your views here.
