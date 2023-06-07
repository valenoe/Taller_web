from django.shortcuts import render
from .models import Usuario
from .form import UsuarioForm
from django.contrib import messages

'''def post_list(request):
    posts = Post.objects.all()
    return render(request, 'fichas/templates/main.html',
{'posts': posts})
'''

def post_list(request):

    posts = Usuario.objects.all()
    if request.method == 'POST':
        post_form = UsuarioForm(request.POST)
        if post_form.is_valid():
            temp = post_form.save(commit=False);
            temp.author = request.user;
            temp.save()
            #post_form.save()
            messages.success(request, "El usuario fue guardado exitosamente")
        else:
            messages.error(request, "ha ocurrido un error al guardar al usuario")
    post_form = UsuarioForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'formulario':post_form})

def login(request):
    return render(request, 'blog/login.html')
