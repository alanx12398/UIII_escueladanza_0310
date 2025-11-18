from django.contrib import admin
from .models import Profesor, Alumno, Clase

# ========================
# ADMIN: PROFESOR
# ========================
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'especialidad', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'especialidad')
    ordering = ('nombre',)


# ========================
# ADMIN: ALUMNO
# ========================
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'nivel', 'telefono', 'correo', 'fecha_inscripcion')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('nivel',)
    ordering = ('nombre',)


# ========================
# ADMIN: CLASE
# ========================
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_clase', 'descripcion', 'horario', 'profesor', 'fecha_inicio')
    search_fields = ('nombre_clase', 'descripcion', 'horario')
    list_filter = ('profesor', 'fecha_inicio')
    ordering = ('nombre_clase',)
