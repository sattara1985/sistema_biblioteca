from django.db import models
from libros.models import Libro

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=200, null=True, blank=True)
    #usuario = models.CharField(max_length=200)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"
