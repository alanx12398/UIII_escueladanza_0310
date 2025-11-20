from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_danza, name='inicio'),

    # PROFESOR CRUD
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/ver/', views.ver_profesores, name='ver_profesores'),
    path('profesores/actualizar/<int:id>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesores/borrar/<int:id>/', views.borrar_profesor, name='borrar_profesor'),

    # ALUMNO CRUD
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/ver/', views.ver_alumnos, name='ver_alumnos'),
    path('alumnos/actualizar/<int:id>/', views.actualizar_alumno, name='actualizar_alumno'),
    path('alumnos/borrar/<int:id>/', views.borrar_alumno, name='borrar_alumno'),

    # CLASES
    path('clases/agregar/', views.agregar_clase, name='agregar_clase'),
    path('clases/ver/', views.ver_clases, name='ver_clases'),
    path('clases/actualizar/<int:id>/', views.actualizar_clase, name='actualizar_clase'),
    path('clases/borrar/<int:id>/', views.borrar_clase, name='borrar_clase'),

    # SALONES
    path('salones/agregar/', views.agregar_salon, name='agregar_salon'),
    path('salones/ver/', views.ver_salones, name='ver_salones'),
    path('salones/actualizar/<int:id>/', views.actualizar_salon, name='actualizar_salon'),
    path('salones/borrar/<int:id>/', views.borrar_salon, name='borrar_salon'),

    # ASISTENCIAS
    path('asistencias/agregar/', views.agregar_asistencia, name='agregar_asistencia'),
    path('asistencias/ver/', views.ver_asistencias, name='ver_asistencias'),
    path('asistencias/actualizar/<int:id>/', views.actualizar_asistencia, name='actualizar_asistencia'),
    path('asistencias/borrar/<int:id>/', views.borrar_asistencia, name='borrar_asistencia'),
]
