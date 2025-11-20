from django.shortcuts import render, redirect, get_object_or_404
from django.middleware.csrf import get_token
from .models import Profesor, Alumno, Clase, Salon, Asistencia

# ==========================
# Inicio
# ==========================
def inicio_danza(request):
    return render(request, 'inicio.html')

# ==========================
# PROFESORES
# ==========================

def agregar_profesor(request):
    if request.method == 'POST':
        Profesor.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            especialidad=request.POST['especialidad'],
            fecha_contratacion=request.POST['fecha_contratacion']
        )
        return redirect('ver_profesores')

    return render(request, 'profesor/agregar_profesor.html')


def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/ver_profesores.html', {
        'profesores': profesores
    })


def actualizar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == "POST":
        profesor.nombre = request.POST['nombre']
        profesor.apellido = request.POST['apellido']
        profesor.telefono = request.POST['telefono']
        profesor.correo = request.POST['correo']
        profesor.especialidad = request.POST['especialidad']
        profesor.fecha_contratacion = request.POST['fecha_contratacion']
        profesor.save()
        return redirect('ver_profesores')

    return render(request, 'profesor/actualizar_profesor.html', {
        'profesor': profesor
    })


def borrar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('ver_profesores')

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
# ALUMNOS
# ==========================

def agregar_alumno(request):
    if request.method == 'POST':
        Alumno.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            correo=request.POST.get('correo'),
            telefono=request.POST.get('telefono'),
            nivel=request.POST.get('nivel'),
            fecha_inscripcion=request.POST.get('fecha_inscripcion')
        )
        return redirect('ver_alumnos')

    return render(request, 'alumno/agregar_alumno.html')


def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/ver_alumnos.html', {
        'alumnos': alumnos
    })


def actualizar_alumno(request, id):
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

    return render(request, 'alumno/actualizar_alumno.html', {
        'alumno': alumno
    })


def borrar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()
    return redirect('ver_alumnos')

# ==========================
# CLASES
# ==========================

def agregar_clase(request):
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        clase = Clase.objects.create(
            nombre_clase=request.POST['nombre_clase'],
            profesor_id=request.POST['profesor'],
            horario=request.POST['horario'],
            fecha_inicio=request.POST['fecha_inicio']
        )
        clase.alumnos.set(request.POST.getlist('alumnos'))
        clase.save()
        return redirect('ver_clases')

    return render(request, 'clase/agregar_clase.html', {
        'profesores': profesores,
        'alumnos': alumnos
    })


def ver_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clase/ver_clases.html', {
        'clases': clases
    })


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
        clase.alumnos.set(request.POST.getlist('alumnos'))
        clase.save()
        return redirect('ver_clases')

    return render(request, 'clase/actualizar_clase.html', {
        'clase': clase,
        'profesores': profesores,
        'alumnos': alumnos
    })


def borrar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    clase.delete()
    return redirect('ver_clases')

# ==========================
# SALONES
# ==========================

def agregar_salon(request):
    if request.method == 'POST':
        Salon.objects.create(
            nombre=request.POST.get('nombre'),
            capacidad=int(request.POST.get('capacidad') or 0),
            ubicacion=request.POST.get('ubicacion'),
            uso=request.POST.get('uso'),
            equipo_disponible=request.POST.get('equipo_disponible')
        )
        return redirect('ver_salones')

    return render(request, 'salon/agregar_salon.html')


def ver_salones(request):
    salones = Salon.objects.all()
    return render(request, 'salon/ver_salones.html', {
        'salones': salones
    })


def actualizar_salon(request, id):
    salon = get_object_or_404(Salon, id=id)

    if request.method == 'POST':
        salon.nombre = request.POST.get('nombre')
        salon.capacidad = int(request.POST.get('capacidad') or 0)
        salon.ubicacion = request.POST.get('ubicacion')
        salon.uso = request.POST.get('uso')
        salon.equipo_disponible = request.POST.get('equipo_disponible')
        salon.save()
        return redirect('ver_salones')

    return render(request, 'salon/actualizar_salon.html', {
        'salon': salon
    })


def borrar_salon(request, id):
    salon = get_object_or_404(Salon, id=id)
    salon.delete()
    return redirect('ver_salones')

# ==========================
# ASISTENCIAS
# ==========================

def agregar_asistencia(request):
    clases = Clase.objects.all()
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        Asistencia.objects.create(
            fecha=request.POST.get('fecha'),
            estado=request.POST.get('estado'),
            clase_id=request.POST.get('clase'),
            alumno_id=request.POST.get('alumno'),
            entrada=request.POST.get('entrada') or None,
            salida=request.POST.get('salida') or None
        )
        return redirect('ver_asistencias')

    return render(request, 'asistencia/agregar_asistencia.html', {
        'clases': clases,
        'alumnos': alumnos
    })


def ver_asistencias(request):
    asistencias = Asistencia.objects.select_related('alumno', 'clase').all()
    return render(request, 'asistencia/ver_asistencias.html', {
        'asistencias': asistencias
    })


def actualizar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    clases = Clase.objects.all()
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        asistencia.fecha = request.POST.get('fecha')
        asistencia.estado = request.POST.get('estado')
        asistencia.clase_id = request.POST.get('clase')
        asistencia.alumno_id = request.POST.get('alumno')
        asistencia.entrada = request.POST.get('entrada') or None
        asistencia.salida = request.POST.get('salida') or None
        asistencia.save()
        return redirect('ver_asistencias')

    return render(request, 'asistencia/actualizar_asistencia.html', {
        'asistencia': asistencia,
        'clases': clases,
        'alumnos': alumnos
    })


def borrar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.delete()
    return redirect('ver_asistencias')
