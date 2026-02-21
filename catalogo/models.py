from django.db import models

class Categoria (models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f"{self.nombre}"


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titulo} - {self.autor}"