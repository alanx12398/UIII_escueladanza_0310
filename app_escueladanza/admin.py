from django.contrib import admin
from .models import Profesor, Alumno, Clase

# Por ahora solo se trabajará con PROFESOR
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'especialidad', 'activo')
    search_fields = ('nombre', 'apellido', 'correo')

# Dejar pendientes los demás modelos
# admin.site.register(Alumno)
# admin.site.register(Clase)
