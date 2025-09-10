
from django.db import models
from django.utils.text import slugify

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Estudiante")
    email = models.EmailField(max_length=254, verbose_name="Correo Electrónico")
    edad = models.IntegerField(verbose_name="Edad del Estudiante")

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    duracion = models.IntegerField(verbose_name="Duración (en meses)")

    def __str__(self):
        return self.nombre_curso