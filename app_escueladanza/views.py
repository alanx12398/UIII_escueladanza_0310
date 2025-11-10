from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor

# ==========================
# Vista de Inicio
# ==========================
def inicio_danza(request):
    return render(request, 'inicio.html')

# ==========================
# Agregar Profesor
# ==========================
def agregar_profesor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        especialidad = request.POST['especialidad']
        fecha_contratacion = request.POST['fecha_contratacion']

        Profesor.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            especialidad=especialidad,
            fecha_contratacion=fecha_contratacion
        )
        return redirect('ver_profesores')

    return render(request, 'profesor/agregar_profesor.html')

# ==========================
# Ver Profesores
# ==========================
def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/ver_profesores.html', {'profesores': profesores})

# ==========================
# Actualizar Profesor
# ==========================
def actualizar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    return render(request, 'profesor/actualizar_profesor.html', {'profesor': profesor})

def realizar_actualizacion_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.nombre = request.POST['nombre']
        profesor.apellido = request.POST['apellido']
        profesor.telefono = request.POST['telefono']
        profesor.correo = request.POST['correo']
        profesor.especialidad = request.POST['especialidad']
        profesor.fecha_contratacion = request.POST['fecha_contratacion']
        profesor.save()
        return redirect('ver_profesores')

# ==========================
# Borrar Profesor
# ==========================
def borrar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('ver_profesores')
