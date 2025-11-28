from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def home(request):
    return render(request, 'libros/home.html')

def lista_libros(request):
    query = request.GET.get("q", "")

    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()

    return render(request, "libros/lista_libros.html", {
        "libros": libros,
        "query": query
    })


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(request, 'libros/crear_libro.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('lista_libros')

