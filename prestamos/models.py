from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Libro

class Prestamo(models.Model):
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    devuelto = models.BooleanField(default=False)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo}"
