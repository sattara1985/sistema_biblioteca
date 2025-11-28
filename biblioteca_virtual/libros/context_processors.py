
from .models import Libro

def total_libros(request):
    """
    Devuelve el conteo total de libros para que esté disponible en todos los templates
    como la variable `total_libros`.
    """
    return {'total_libros': Libro.objects.count()}
