from django.shortcuts import render, redirect
from .models import *
from .forms import UsuarioForm

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
