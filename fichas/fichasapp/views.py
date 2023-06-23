from django.shortcuts import render, redirect
from .models import *
from fichasapp.forms import *
from django.shortcuts import get_object_or_404


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
    return render(request, 'especialidad/especialidad.html', {'especialidad': especialidad})

def create_especialidad(request):
    form = EspecialidadForm()
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')

    context = {'form': form}
    return render(request, 'especialidad/especialidad_form.html', context)


def edit_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    form = EspecialidadForm(instance=especialidad)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('/especialidad')
    context = {'form': form}
    return render(request, 'especialidad/especialidad_form.html', context)


def delete_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    if request.method == "POST":
        especialidad.delete()
        return redirect('/especialidad')
    context = {'especialidad': especialidad}
    return render(request, 'especialidad/eliminar_especialidad.html', context)

def view_especialidad(request, pk):
    especialidad = Especialidad.objects.get(id=pk)
    context = {
        'especialidad': especialidad
    }
    return render(request, 'especialidad/mostrar_especialidad.html', context)

def fichas(request):
    fichas = Ficha.objects.all()
    context = {
        'fichas': fichas,
    }
    return render(request, 'fichas/fichas.html', context)


def create_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fichas')
    else:
        form = FichaForm()

    context = {
        'form': form,
    }
    return render(request, 'fichas/ficha_form.html', context)


def delete_ficha(request, pk):
    ficha = get_object_or_404(Ficha, id=pk)
    if request.method == 'POST':
        ficha.delete()
        return redirect('fichas')

    context = {
        'ficha': ficha,
    }
    return render(request, 'fichas/delete_ficha.html', context)


def view_ficha(request, pk):
    ficha = Ficha.objects.get(id=pk)
    context = {'ficha': ficha}
    return render(request, 'fichas/view_ficha.html', context)


def edit_ficha(request, pk):
    ficha = Ficha.objects.get(id=pk)
    form = FichaForm(instance=ficha)
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('/fichas')
    context = {'form': form}
    return render(request, 'fichas/ficha_form.html', context)

def login(request):
    return render(request, '/login.html')
