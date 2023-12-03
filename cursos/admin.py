from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Leccion, UserProfile

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Leccion)
admin.site.register(UserProfile)

