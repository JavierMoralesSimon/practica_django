from django.shortcuts import render, redirect
from .models import Libro, Categoria
from .forms import LibroForm, CategoriaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    '''
    Lista todos los libros y categorías existentes.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con la lista de libros y categorías.
    '''
    libros=Libro.objects.all()
    categorias=Categoria.objects.all()
    return render(request, 'catalogo/index.html', {'libros': libros, 'categorias': categorias})

@login_required
def libros_crear(request):
    '''
    Crea un libro.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con un formulario para crear un libro o con la lista de libros y categorías.
    '''
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El libro se creó con éxito.")
        else:
            messages.error(request, "No se pudo crear el libro.")
        return redirect('catalogo.index')
    else:
        form = LibroForm()
    return render(request, 'catalogo/libros/crear.html', {'form': form})

@login_required
def libros_actualizar(request, id):
    '''
    Actualiza un libro.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id del libro a actualizar.
    Retorna:
        HttpResponse: Página HTML con un formulario para actualizar un libro o con la lista de libros y categorías.
    '''
    libro=Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "El libro se actualizó con éxito.")
        else:
            messages.error(request, "No se pudo actualizar el libro.")
        return redirect('catalogo.index')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'catalogo/libros/actualizar.html', {'form': form, 'libro': libro})

@login_required
def libros_borrar(request, id):
    '''
    Borra un libro.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id del libro a borrar.
    Retorna:
        HttpResponse: Página HTML con una confirmación de borrado de un libro o con la lista de libros y categorías.
    '''
    libro=Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "El libro se borró con éxito.")
        return redirect('catalogo.index')
    elif not libro.disponible:
        messages.error(request, "Actualmente no se puede borrar el libro indicado porque está prestado.")
        return redirect('catalogo.index')
    return render(request, 'catalogo/libros/borrar.html', {'libro': libro})

@login_required
def categorias_crear(request):
    '''
    Crea una categoría.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
    Retorna:
        HttpResponse: Página HTML con un formulario para crear una categoría o con la lista de libros y categorías.
    '''
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La categoría se creó con éxito.")
        else:
            messages.error(request, "No se pudo crear la categoría.")
        return redirect('catalogo.index')
    else:
        form = CategoriaForm()
    return render(request, 'catalogo/categorias/crear.html', {'form': form})

@login_required
def categorias_actualizar(request, id):
    '''
    Actualiza una categoría.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id de la categoría a actualizar.
    Retorna:
        HttpResponse: Página HTML con un formulario para actualizar un libro o con la lista de libros y categorías.
    '''
    categoria=Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "La categoría se actualizó con éxito.")
        else:
            messages.error(request, "No se pudo actualizar la categoría.")
        return redirect('catalogo.index')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'catalogo/categorias/actualizar.html', {'form': form, 'categoria': categoria})

@login_required
def categorias_borrar(request, id):
    '''
    Borra una categoría.
    Parámetros:
        request (HttpRequest): Objeto que representa la petición HTTP.
        id (int): Número entero que representa el id de la categoría a borrar.
    Retorna:
        HttpResponse: Página HTML con una confirmación de borrado de una categoría o con la lista de libros y categorías.
    '''
    categoria=Categoria.objects.get(id=id)
    libros_prestados=Libro.objects.filter(disponible=False, categoria=categoria)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, "La categoría se borró con éxito.")
        return redirect('catalogo.index')
    elif len(libros_prestados)>0:
        if len(libros_prestados)==1:
            messages.error(request, "Actualmente no se puede borrar la categoria indicada porque existe un libro prestado que usa la misma.")
        else:
            messages.error(request, f"Actualmente no se puede borrar la categoria indicada porque existen {len(libros_prestados)} libros prestados que usan la misma.")
        return redirect('catalogo.index')
    return render(request, 'catalogo/categorias/borrar.html', {'categoria': categoria})
