from django.urls import path
from .views import lista_libros, crear_libro, editar_libro, eliminar_libro

urlpatterns = [
    path('', lista_libros, name='lista_libros'),
    path('crear/', crear_libro, name='crear_libro'),
    path('editar/<int:id>/', editar_libro, name='editar_libro'),
    path('eliminar/<int:id>/', eliminar_libro, name='eliminar_libro'),
]
