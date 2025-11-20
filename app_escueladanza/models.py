from django.db import models
from datetime import date

# --- PROFESOR (mantener el tuyo) ---
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# --- ALUMNO (mantener el tuyo) ---
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    nivel = models.CharField(max_length=30, choices=[
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado')
    ])
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# --- SALON (nuevo) ---
class Salon(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=150, blank=True)
    uso = models.CharField(max_length=100, blank=True)
    equipo_disponible = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nombre}"


# --- CLASE (actualizado) ---
class Clase(models.Model):
    # antes tenías nombre_clase; lo dejamos así
    nombre_clase = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=50, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="clases")
    alumnos = models.ManyToManyField(Alumno, related_name="clases", blank=True)
    fecha_inicio = models.DateField(default=date.today)
    salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, blank=True, related_name="clases")

    def __str__(self):
        return self.nombre_clase


# --- ASISTENCIA (nuevo) ---
class Asistencia(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=50)      # ejemplo: Presente, Ausente, Tarde
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="asistencias")
    entrada = models.TimeField(null=True, blank=True)
    salida = models.TimeField(null=True, blank=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="asistencias")

    def __str__(self):
        return f"Asistencia: {self.alumno} - {self.clase} - {self.fecha}"
