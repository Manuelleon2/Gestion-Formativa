from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:estudiante_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/editar/<int:profesor_id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:profesor_id>/', views.eliminar_profesor, name='eliminar_profesor'),

    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),

    path('lecciones/', views.lista_lecciones, name='lista_lecciones'),
    path('lecciones/agregar/', views.agregar_leccion, name='agregar_leccion'),
    path('lecciones/editar/<int:leccion_id>/', views.editar_leccion, name='editar_leccion'),
    path('lecciones/eliminar/<int:leccion_id>/', views.eliminar_leccion, name='eliminar_leccion'),

    path('', auth_views.LoginView.as_view(template_name='cursos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('registro/', views.registrar_usuario, name='registro_usuario'),
    path('index/', views.index, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
