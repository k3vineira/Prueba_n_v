from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='articulos')

    def __str__(self):
        return self.titulo

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.IntegerField(unique=True, max_length=10)
    def __str__(self):
        return self.nombre
    
class curso(models.Model):
    codigo = models.CharField(max_length=10)
    titulo = models.CharField(max_length=100)
    abierto = models.BooleanField(default=True)
    Estudiante = models.ForeignKey("Estudiante", related_name="Cursos", blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"
    

