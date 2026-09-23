from django.shortcuts import render
from .models import Autor, Articulo, Estudiante, curso

def index(request):
    autor = Autor.objects.all()
    articulo = Articulo.objects.all()
    estudiante = Estudiante.objects.all()
    curso = curso.objects.all()
    return render(request, 'index.html')
