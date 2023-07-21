from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import JsonResponse


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
        return redirect('usuarios')
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
    usuarios = Usuario.objects.all
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


def create_horas(request):
    if request.method == 'POST':
        form = HorasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horas')
    else:
        form = HorasForm()
    return render(request, 'horas\horas_form.html', {'form': form})


def horas(request):
    horas = Horas.objects.all()
    return render(request, 'horas/horas.html', {'horas': horas})


def get_horario_choices(request):
    if request.method == 'GET' and 'id_medico' in request.GET:
        id_medico_id = request.GET.get('id_medico')
        horarios = Horas.objects.filter(id_medico_id=id_medico_id, ocupada=False)
        horario_choices = [(horario.pk, str(horario)) for horario in horarios]
        return JsonResponse(horario_choices, safe=False)
    return JsonResponse([], safe=False)


def edit_hora(request, pk):
    hora = Horas.objects.get(id=pk)
    if request.method == 'POST':
        form = HorasForm(request.POST, instance=hora)
        if form.is_valid():
            form.save()
            return redirect('horas')
    else:
        form = HorasForm(instance=hora)
    return render(request, 'horas\horas_form.html', {'form': form})


def view_hora(request, pk):
    hora = Horas.objects.get(id=pk)
    context = {'hora': hora}
    return render(request, 'horas/view_hora.html', context)


def delete_hora(request, pk):
    hora = get_object_or_404(Horas, id=pk)
    if request.method == 'POST':
        hora.delete()
        return redirect('horas')

    context = {
        'hora': hora,
    }
    return render(request, 'horas/delete_hora.html', context)


def create_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas')  # Replace 'success_url' with the URL to redirect after successful form submission
    else:
        form = CitaForm()
    return render(request, 'citas/cita_form.html', {'form': form})

def view_cita(request, pk):
    cita = get_object_or_404(Cita, id=pk)
    return render(request, 'citas/view_cita.html', {'cita': cita})

def citas(request):
    citas = Cita.objects.all()
    context = {'citas': citas}
    return render(request, 'citas/citas.html', context)

def edit_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/cita_form.html', {'form': form})

def delete_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.id_horario.ocupada = False
        cita.id_horario.save()
        cita.delete()
        return redirect('citas')
    return render(request, 'citas/delete_cita.html', {'cita': cita})

def lista_datos_atencion(request):
    datos_atencion_list = DatosAtencion.objects.all()
    return render(request, 'atencion/lista_datos_atencion.html', {'datos_atencion_list': datos_atencion_list})

def crear_datos_atencion(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    
    # Verificar si ya existe un registro de DatosAtencion para esta cita
    datos_atencion_existente = DatosAtencion.objects.filter(id_cita=cita_id).first()
    if datos_atencion_existente:
        return redirect('lista_datos_atencion')
    
    if request.method == 'POST':
        form = DatosAtencionForm(request.POST)
        if form.is_valid():
            datos_atencion = form.save(commit=False)
            datos_atencion.id_cita = cita
            datos_atencion.save()
            return redirect('lista_datos_atencion')
    else:
        form = DatosAtencionForm()
    return render(request, 'atencion/crear_datos_atencion.html', {'form': form, 'cita': cita})

def detalle_datos_atencion(request, datos_atencion_id):
    datos_atencion = get_object_or_404(DatosAtencion, pk=datos_atencion_id)
    return render(request, 'atencion/detalle_datos_atencion.html', {'datos_atencion': datos_atencion})

def modificar_datos_atencion(request, datos_atencion_id):
    datos_atencion = get_object_or_404(DatosAtencion, pk=datos_atencion_id)
    if request.method == 'POST':
        form = DatosAtencionForm(request.POST, instance=datos_atencion)
        if form.is_valid():
            form.save()
            return redirect('lista_datos_atencion')
    else:
        form = DatosAtencionForm(instance=datos_atencion)
    return render(request, 'atencion/crear_datos_atencion.html', {'form': form, 'datos_atencion': datos_atencion})

def eliminar_datos_atencion(request, datos_atencion_id):
    datos_atencion = get_object_or_404(DatosAtencion, pk=datos_atencion_id)
    if request.method == 'POST':
        datos_atencion.delete()
        return redirect('citas')  # Assuming 'citas' is the URL name for the Cita list view
    return render(request, 'atencion/eliminar_datos_atencion.html', {'datos_atencion': datos_atencion})

def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'roles/listar_roles.html', {'roles': roles})

def crear_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_roles')
    else:
        form = RolForm()
    return render(request, 'roles/crear_rol.html', {'form': form})

def ver_rol(request, rol_id):
    rol = get_object_or_404(Rol, pk=rol_id)
    return render(request, 'roles/ver_rol.html', {'rol': rol})

def modificar_rol(request, rol_id):
    rol = get_object_or_404(Rol, pk=rol_id)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('listar_roles')
    else:
        form = RolForm(instance=rol)
    return render(request, 'roles/modificar_rol.html', {'form': form, 'rol': rol})

def eliminar_rol(request, rol_id):
    rol = get_object_or_404(Rol, pk=rol_id)
    if request.method == 'POST':
        rol.delete()
        return redirect('listar_roles')
    return render(request, 'roles/eliminar_rol.html', {'rol': rol})

def crear_paciente(request):
    if request.method == 'POST':
        form = UsuarioPacienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol = Rol.objects.get(name='Paciente')
            usuario.save()
            return redirect('ficha_paciente', pk=usuario.pk)  
    else:
        form = UsuarioPacienteForm(initial={'rol': Rol.objects.get(name='Paciente')})  

    context = {'form': form}
    return render(request, 'paciente/crear_paciente.html', context)

def ficha_paciente(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        form = FichaPacienteForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.usuario = usuario
            ficha.save()
            return redirect('cita_paciente', pk=ficha.pk)  
    else:
        form = FichaPacienteForm(initial={'usuario': usuario})  

    context = {'form': form}
    return render(request, 'paciente/ficha_paciente.html', context)

def cita_paciente(request, pk):
    ficha = get_object_or_404(Ficha, pk=pk)

    if request.method == 'POST':
        form = CitaPacienteForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = ficha.usuario
            cita.save()
            return redirect('/citas')  
    else:
        form = CitaPacienteForm(initial={'usuario': ficha.usuario})  

    context = {'form': form}
    return render(request, 'paciente/cita_paciente.html', context)

