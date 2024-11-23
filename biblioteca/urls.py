from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),  # Página principal
    path('libros/', views.lista_libros, name='lista_libros'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('generos/', views.lista_generos, name='lista_generos'),
    path('buscar/', views.buscar_libros, name='buscar_libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
]
