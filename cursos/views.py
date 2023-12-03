from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Leccion, UserProfile
from .forms import EstudianteForm, ProfesorForm, CursoForm, LeccionForm, UserForm, UserProfileForm
from django.contrib.auth.models import User

# Vistas Estudiantes --------------------------------------------------

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'cursos/lista_estudiantes.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'cursos/agregar_estudiante.html', {'form': form})

def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'cursos/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'cursos/eliminar_estudiante.html', {'estudiante': estudiante})

# Vistas Profesores -----------------------------------------------

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'cursos/lista_profesores.html', {'profesores': profesores})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'cursos/agregar_profesor.html', {'form': form})

def editar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'cursos/editar_profesor.html', {'form': form, 'profesor': profesor})

def eliminar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('lista_profesores')
    return render(request, 'cursos/eliminar_profesor.html', {'profesor': profesor})

# Resto de vistas de Cursos -------------------------------------------

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/agregar_curso.html', {'form': form})

def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form, 'curso': curso})

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})

# vistas de Lecciones ----------------------------------------

def lista_lecciones(request):
    lecciones = Leccion.objects.all()
    return render(request, 'cursos/lista_lecciones.html', {'lecciones': lecciones})

def agregar_leccion(request):
    if request.method == 'POST':
        form = LeccionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_lecciones')
    else:
        form = LeccionForm()
    return render(request, 'cursos/agregar_leccion.html', {'form': form})

def editar_leccion(request, leccion_id):
    leccion = get_object_or_404(Leccion, pk=leccion_id)
    if request.method == 'POST':
        form = LeccionForm(request.POST, instance=leccion)
        if form.is_valid():
            form.save()
            return redirect('lista_lecciones')
    else:
        form = LeccionForm(instance=leccion)
    return render(request, 'cursos/editar_leccion.html', {'form': form, 'leccion': leccion})

def eliminar_leccion(request, leccion_id):
    leccion = get_object_or_404(Leccion, pk=leccion_id)
    if request.method == 'POST':
        leccion.delete()
        return redirect('lista_lecciones')
    return render(request, 'cursos/eliminar_leccion.html', {'leccion': leccion})

# Vistas de Usuario

def registrar_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'registro_usuario.html', {'user_form': user_form, 'profile_form': profile_form})

def index(request):
    return render(request, 'cursos/index.html')

