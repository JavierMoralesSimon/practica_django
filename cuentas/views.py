from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, ContactoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    '''
    Página principal de la aplicación.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con botones para inicio de sesión y registro.
    '''
    return render(request, 'cuentas/index.html')

def register_usuario(request):
    '''
    Registra un usuario.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con un formulario para registrar un usuario o con la lista de préstamos personales y libros disponibles.
    '''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if username.lower() == "admin":
                form.add_error('username', "El nombre de usuario 'admin' no está permitido.")
            else:
                user = form.save()
                login(request, user)
                return redirect('/prestamos/index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cuentas/register.html', {'form': form})

def login_usuario(request):
    '''
    Loguea un usuario.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con un formulario para loguear un usuario o con la lista de libros y categorías o con la lista de préstamos personales y libros disponibles.
    '''
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            if usuario.username.lower() == "admin":
                return redirect("/catalogo/index")
            else:
                return redirect("/prestamos/index")
    else:
        form = AuthenticationForm()
    return render(request, "cuentas/login.html", {"form": form})

@login_required
def logout_usuario(request):
    '''
    Cierra la sesión de un usuario.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Redirección a la página principal de la aplicación.
    '''
    logout(request)
    return redirect("/")

@login_required
def contacto(request):
    '''
    Opción de contacto de un usuario con los dueños de la página.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con un formulario para contactar a los dueños de la página o con la lista de préstamos personales y libros disponibles.
    '''
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            messages.success(request, "El mensaje se envió con éxito.")
        else:
            messages.error(request, "No se pudo enviar el mensaje.")
        return redirect('/prestamos/index')
    else:
        form = ContactoForm()
    return render(request, 'cuentas/contacto.html', {'form': form})