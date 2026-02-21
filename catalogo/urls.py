from django.urls import path
from catalogo import views as v

urlpatterns = [
    path('index/', v.index, name='catalogo.index'),
    path('libros/crear/', v.libros_crear, name='libros.crear'),
    path('libros/actualizar/<int:id>/', v.libros_actualizar, name='libros.actualizar'),
    path('libros/borrar/<int:id>/', v.libros_borrar, name='libros.borrar'),
    path('categorias/crear/', v.categorias_crear, name='categorias.crear'),
    path('categorias/actualizar/<int:id>/', v.categorias_actualizar, name='categorias.actualizar'),
    path('categorias/borrar/<int:id>/', v.categorias_borrar, name='categorias.borrar'),
]