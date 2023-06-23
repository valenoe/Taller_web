from django.shortcuts import render, redirect
from .models import *
from fichasapp.forms import UsuarioForm, PersonalSaludForm, EspecialidadForm


def home(request):
    return render(request, 'fichas/index.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})



def create_usuario(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usuarios')

    context = {'form': form}
    return render(request, 'usuarios/user_form.html', context)


def edit_usuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/usuarios')
    context = {'form': form}
    return render(request, 'usuarios/user_form.html', context)


def delete_usuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('/usuarios')
    context = {'usuario': usuario}
    return render(request, 'usuarios/delete_usuario.html', context)


def view_usuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    context = {'usuario': usuario}
    return render(request, 'usuarios/view_usuario.html', context)

def personalSalud(request):
    personal = PersonalSalud.objects.all()
    return render(request, 'personalSalud/psalud.html', {'personal': personal})

def create_personalSalud(request):
    form = PersonalSaludForm()
    if request.method == 'POST':
        form = PersonalSaludForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personalsalud')

    context = {'form': form}
    return render(request, 'personalSalud/personal_form.html', context)

def edit_personalSalud(request, pk):
    personal = PersonalSalud.objects.get(id=pk)
    form = UsuarioForm(instance=personal)
    if request.method == 'POST':
        form = PersonalSaludForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('/personalsalud')
    context = {'form': form}
    return render(request, 'personalSalud/personal_form.html', context)


def delete_personalSalud(request, pk):
    personal = PersonalSalud.objects.get(id=pk)
    if request.method == "POST":
        personal.delete()
        return redirect('/personalsalud')
    context = {'personal': personal}
    return render(request, 'personalSalud/eliminar_personal.html', context)
def view_personalSalud(request, pk):
    personal = PersonalSalud.objects.get(id=pk)
    usuario = personal.usuario_id  # Acceder al objeto Usuario relacionado
    context = {
        'personal': personal,
        'usuario': usuario
    }
    return render(request, 'personalSalud/mostrar_personal.html', context)



def especialidad(request):
    especialidad = Especialidad.objects.all()
    return render(request, 'fichas/especialidad.html', {'especialidad': especialidad})

def create_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')

    context = {'form': form}
    return render(request, 'fichas/especialidad_form.html', context)


def edit_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    form = EspecialidadForm(instance=especialidad)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')
    context = {'form': form}
    return render(request, 'fichas/especialidad_form.html', context)


def delete_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    if request.method == "POST":
        especialidad.delete()
        return redirect('/especialidad')
    context = {'especialidad': especialidad}
    return render(request, 'fichas/eliminar_especialidad.html', context)

def view_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    context = {
        'especialidad': especialidad
    }
    return render(request, 'fichas/mostrar_especialidad.html', context)

