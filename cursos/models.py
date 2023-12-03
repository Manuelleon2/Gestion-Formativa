from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

class Profesor(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesores = models.ManyToManyField(Profesor, related_name='cursos')
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
    
    def __str__(self):
        return self.nombre

class Leccion(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, related_name='lecciones', on_delete=models.CASCADE)
    descripcion_actividad = models.TextField()
    contenido = models.FileField(upload_to='contenido_lecciones/')

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
        ('administrador', 'Administrador'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)


