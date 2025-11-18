from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_danza, name='inicio'),

    # PROFESOR CRUD
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/ver/', views.ver_profesores, name='ver_profesores'),
    path('profesores/actualizar/<int:id>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesores/actualizar/<int:id>/guardar/', views.realizar_actualizacion_profesor, name='realizar_actualizacion_profesor'),
    path('profesores/borrar/<int:id>/', views.borrar_profesor, name='borrar_profesor'),


    # ALUMNO CRUD
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/ver/', views.ver_alumnos, name='ver_alumnos'),
    path('alumnos/actualizar/<int:id>/', views.actualizar_alumno, name='actualizar_alumno'),
    path('alumnos/actualizar/<int:id>/guardar/', views.realizar_actualizacion_alumno, name='realizar_actualizacion_alumno'),
    path('alumnos/borrar/<int:id>/', views.borrar_alumno, name='borrar_alumno'),


        # CLASES (nuevas)
    path('clases/agregar/', views.agregar_clase, name='agregar_clase'),
    path('clases/', views.ver_clases, name='ver_clases'),
    path('clases/actualizar/<int:id>/', views.actualizar_clase, name='actualizar_clase'),
    path('clases/borrar/<int:id>/', views.borrar_clase, name='borrar_clase'),
]