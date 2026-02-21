# El Rincón del Lector 📖

## Descripción breve del proyecto
El proyecto está basado en una biblioteca en la que un super usuario administrador tiene el poder de realizar las operaciones de crear, actualizar y borrar tanto libros como las categorías en las que estos mismos se encuentran. Por otro lado, se encuentran los usuarios "normales", los cuales pueden acceder al catálogo de libros disponibles para alquilar y decidir si realizar préstamos de ellos o devolver los que ya le fueron prestados.

## Cómo ejecutar el proyecto
El primer paso para una exitosa ejecución del proyecto es la instalación de Python si no lo tenemos instalado ya. Posteriormente, este repositorio el cual incluye el proyecto, se clonaría y con él nos conectaríamos a un entorno virtual previamente creado si es que decidimos usar esto como área de trabajo y no nuestro ordenador local. Por último, en la área elegida ejecutaríamos los siguientes comandos aunque de nuevo, si los que involucran instalar algo, ya tenemos eso instalado, se omitirían:
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
