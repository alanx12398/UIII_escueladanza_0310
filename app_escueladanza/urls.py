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
]
