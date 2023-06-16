from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from fichasapp.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')


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