from django.contrib import admin
from .models import Profesor, Alumno, Clase, Salon, Asistencia

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'especialidad', 'telefono', 'correo', 'activo')
    search_fields = ('nombre', 'apellido', 'especialidad')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'nivel', 'correo')
    search_fields = ('nombre', 'apellido', 'correo')

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'capacidad', 'ubicacion')
    search_fields = ('nombre',)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_clase', 'profesor', 'salon', 'fecha_inicio')
    search_fields = ('nombre_clase', 'profesor__nombre', 'profesor__apellido')
    filter_horizontal = ('alumnos',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'alumno', 'clase', 'estado', 'entrada', 'salida')
    search_fields = ('alumno__nombre', 'clase__nombre_clase')
    list_filter = ('fecha', 'estado')

