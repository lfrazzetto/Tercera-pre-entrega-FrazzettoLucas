from django import forms
from .models import Libro, Autor, Genero


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero']


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad']


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
