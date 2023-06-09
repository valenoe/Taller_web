from django.shortcuts import render, redirect
from .models import Usuario
from .form import UsuarioForm
from django.contrib import messages

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
            messages.success(request, "El usuario fue guardado exitosamente")
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
            messages.success(request, "El usuario fue modificado exitosamente")
            return redirect('/usuario')
    context = {'form': form}
    return render(request, 'fichas/user_form.html', context)

def eliminarUsuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('/usuario')
    messages.success(request, "El usuario fue eliminado exitosamente")
    context = {'usuario': usuario}
    return render(request, 'fichas/eliminar.html', context)

