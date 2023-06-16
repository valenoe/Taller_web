from django.shortcuts import render, redirect
from .models import *
from fichasapp.forms import UsuarioForm, PersonalSaludForm, EspecialidadForm


def home(request):
    return render(request, 'fichas/index.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'fichas/usuario.html', {'usuarios': usuarios})

def crearUsuario(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usuario')

    context = {'form': form}
    return render(request, 'fichas/user_form.html', context)

def modificarUsuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/usuario')
    context = {'form': form}
    return render(request, 'fichas/user_form.html', context)


def eliminarUsuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('/usuario')
    context = {'usuario': usuario}
    return render(request, 'fichas/eliminar.html', context)
def mostrar_usuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    context = {'usuario': usuario}
    return render(request, 'fichas/mostrar_usuario.html', context)


def personalSalud(request):
    personalsalud = PersonalSalud.objects.all()
    return render(request, 'fichas/psalud.html', {'personalsalud': personalsalud})

def crearPersonal(request):
    form = PersonalSaludForm()
    if request.method == 'POST':
        form = PersonalSaludForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personalsalud')

    context = {'form': form}
    return render(request, 'fichas/personal_form.html', context)

def modificarPersonal(request, pk):
    personal = PersonalSaludForm.objects.get(id=pk)
    form = UsuarioForm(instance=personal)
    if request.method == 'POST':
        form = PersonalSaludForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('/personalsalud')
    context = {'form': form}
    return render(request, 'fichas/personal_form.html', context)


def eliminarPersonal(request, pk):
    personal = PersonalSaludForm.objects.get(id=pk)
    if request.method == "POST":
        personal.delete()
        return redirect('/personalsalud')
    context = {'personal': personal}
    return render(request, 'fichas/eliminar_personal.html', context)
def mostrar_personal(request, pk):
    usuario = Usuario.objects.get(id=pk)
    context = {'usuario': usuario}
    return render(request, 'fichas/mostrar_usuario.html', context)



def especialidad(request):
    especialidad = Especialidad.objects.all()
    return render(request, 'fichas/especialidad.html', {'especialidad': especialidad})

def crear_especialidad(request):
    form = EspecialidadForm()
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')

    context = {'form': form}
    return render(request, 'fichas/especialidad_form.html', context)


def modificarEspecialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    form = EspecialidadForm(instance=especialidad)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')
    context = {'form': form}
    return render(request, 'fichas/especialidad_form.html', context)


def eliminarEspecialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    if request.method == "POST":
        especialidad.delete()
        return redirect('/especialidad')
    context = {'especialidad': especialidad}
    return render(request, 'fichas/eliminar_especialidad.html', context)
