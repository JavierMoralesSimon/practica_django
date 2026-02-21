# Proyecto de biblioteca en Django

## Descripción breve del proyecto
El proyecto está basado en una biblioteca en la que un super usuario administrador tiene el poder de realizar las operaciones de crear, actualizar y borrar tanto libros como las categorías en las que estos mismos se basan. Después, se encuentran los usuarios "normales", los cuales pueden acceder al catálogo de libros disponibles para alquilar y decidir si realizar préstamos de ellos o de devolver los que ya le fueron prestados.

## Cómo ejecutar el proyecto
El primer paso para una exitosa ejecución del proyecto es la instalación de Python y posteriormente la creación de un entorno virtual, si no se tiene acceso ya a uno, y conectarse a él o trabajar en local. Después, en la opción elegida ejecutar los siguientes comandos. Algunos instalan cosas que igual se tienen ya en nuestro área de trabajo por lo que estos se omitirian:
 * Instalacion de Django: `pip install Django`.
 * Instalación de crispy forms:
  * `pip install django-crispy-forms`
  * `pip install crispy-bootstrap5`
 * Ejecución del proyecto: `python manage.py runserver`

## Usuarios de prueba
* Super usuario:
  * Nombre: admin
  * Contraseña: @ad1234min
* Usuario normal:
  * Nombre: user
  * Contraseña: @us1234er
