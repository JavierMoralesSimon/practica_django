from django.shortcuts import render, redirect
from .models import Prestamo
from catalogo.models import Libro
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    '''
    Lista todos los préstamos personales y libros disponibles.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con la lista de préstamos personales y libros disponibles.
    '''
    prestamos=Prestamo.objects.filter(usuario=request.user)
    libros = Libro.objects.exclude(prestamo__usuario=request.user)
    return render(request, 'prestamos/index.html', {'prestamos': prestamos, 'libros': libros})

@login_required
def prestamos_crear(request, id):
    '''
    Crea un préstamo.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id del libro a prestar.
    Retorna:
        HttpResponse: Página HTML con una confirmación de creación de un préstamo o con la lista de préstamos personales y libros disponibles.
    '''
    libro=Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.disponible=False
        libro.save()
        Prestamo.objects.create(
            devuelto = False,
            libro = libro,
            usuario = request.user
        )
        messages.success(request, "El libro se alquiló con éxito.")
        return redirect('prestamos.index')
    return render(request, 'prestamos/crear.html', {'libro': libro})

@login_required
def prestamos_actualizar(request, id):
    '''
    Actualiza un préstamo.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id del préstamo a actualizar.
    Retorna:
        HttpResponse: Página HTML con una confirmación de devolución de un libro o con la lista de préstamos personales y libros disponibles.
    '''
    prestamo=Prestamo.objects.get(id=id)
    libro=prestamo.libro
    if request.method == 'POST':
        libro.disponible=True
        libro.save()
        prestamo.delete()
        messages.success(request, "El libro se devolvió con éxito.")
        return redirect('prestamos.index')
    return render(request, 'prestamos/actualizar.html', {'libro': libro, 'prestamo': prestamo})