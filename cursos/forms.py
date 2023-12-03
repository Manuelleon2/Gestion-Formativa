from django import forms
from .models import Estudiante, Profesor, Curso, Leccion, UserProfile
from django.contrib.auth.models import User

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['identificacion', 'nombre', 'apellido']
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['identificacion', 'nombre', 'apellido']
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'profesores', 'estudiantes']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'profesores': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'estudiantes': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields = ['nombre', 'curso', 'descripcion_actividad', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'descripcion_actividad': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contenido': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_type', )
