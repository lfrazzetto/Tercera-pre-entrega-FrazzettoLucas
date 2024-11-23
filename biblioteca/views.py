from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro, Autor, Genero
from .forms import LibroForm, AutorForm, GeneroForm

# Create your views here.


def inicio(request):
    return HttpResponse("¡Bienvenido a la Biblioteca Digital!")


# Vista para listar libros
def lista_libros(request):
    libros = Libro.objects.all()  # Veo todos los libros
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

# Vista para listar autores


def lista_autores(request):
    autores = Autor.objects.all()  # Veo todos los autores
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})

# Vista para listar géneros


def lista_generos(request):
    generos = Genero.objects.all()  # Veo todos los generos
    return render(request, 'biblioteca/lista_generos.html', {'generos': generos})


def buscar_libros(request):
    query = request.GET.get('q', '')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)  # Busco libros
    else:
        libros = Libro.objects.all()  # Si no hay búsqueda, mostrar todos los libros
    return render(request, 'biblioteca/buscar_libros.html', {'libros': libros, 'query': query})

# Pagina principal


def pagina_principal(request):
    return render(request, 'biblioteca/pagina_principal.html')


## FORMULARIOS ###
# Vista para agregar un nuevo libro
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirijo a lista de libros
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})

# Vista para agregar un nuevo autor


def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/agregar_autor.html', {'form': form})

# Vista para agregar un nuevo género


def agregar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_generos')
    else:
        form = GeneroForm()
    return render(request, 'biblioteca/agregar_genero.html', {'form': form})
