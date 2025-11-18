from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor, Alumno, Clase
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

# AGREGAR ALUMNO
def agregar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        nivel = request.POST.get('nivel')
        fecha_inscripcion = request.POST.get('fecha_inscripcion')

        Alumno.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            nivel=nivel,
            fecha_inscripcion=fecha_inscripcion
        )
        return redirect('ver_alumnos')

    return render(request, 'alumno/agregar_alumno.html')


# VER ALUMNOS
def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/ver_alumnos.html', {'alumnos': alumnos})


# ACTUALIZAR ALUMNO (formulario)
def actualizar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'alumno/actualizar_alumno.html', {'alumno': alumno})


# GUARDAR ACTUALIZACION
def realizar_actualizacion_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido = request.POST.get('apellido')
        alumno.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        alumno.correo = request.POST.get('correo')
        alumno.telefono = request.POST.get('telefono')
        alumno.nivel = request.POST.get('nivel')
        alumno.fecha_inscripcion = request.POST.get('fecha_inscripcion')
        alumno.save()
        return redirect('ver_alumnos')


# BORRAR ALUMNO (confirmación y borrado)
def borrar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('ver_alumnos')
    return render(request, 'alumno/borrar_alumno.html', {'alumno': alumno})

# === AGREGAR CLASE ===
def agregar_clase(request):
    if request.method == 'POST':
        nombre_clase = request.POST['nombre_clase']
        descripcion = request.POST['descripcion']
        horario = request.POST['horario']
        profesor_id = request.POST['profesor']
        alumnos_ids = request.POST.getlist('alumnos')
        fecha_inicio = request.POST['fecha_inicio']

        profesor = Profesor.objects.get(id=profesor_id)

        # CORRECCIÓN: el modelo se llama Clase, no clase
        clase = Clase.objects.create(
            nombre_clase=nombre_clase,
            descripcion=descripcion,
            horario=horario,
            profesor=profesor,
            fecha_inicio=fecha_inicio
        )

        # Asignar alumnos
        clase.alumnos.set(alumnos_ids)

        return redirect('ver_clases')

    # Mostrar formulario
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()
    return render(request, 'clase/agregar_clase.html', {'profesores': profesores, 'alumnos': alumnos})


# === VER CLASES ===
def ver_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clase/ver_clases.html', {'clases': clases})

# === ACTUALIZAR CLASE ===
def actualizar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        clase.nombre_clase = request.POST['nombre_clase']
        clase.descripcion = request.POST['descripcion']
        clase.horario = request.POST['horario']
        clase.profesor_id = request.POST['profesor']
        clase.fecha_inicio = request.POST['fecha_inicio']
        clase.save()
        clase.alumnos.set(request.POST.getlist('alumnos'))
        return redirect('ver_clases')

    return render(request, 'clase/actualizar_clase.html', {'clase': clase, 'profesores': profesores, 'alumnos': alumnos})

# === BORRAR CLASE ===
def borrar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        clase.delete()
        return redirect('ver_clases')
    return render(request, 'clase/borrar_clase.html', {'clase': clase})