from django.db import models

# ==========================================
# MODELO: PROFESOR
# ==========================================
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=50, help_text="Tipo de danza que enseña")
    fecha_contratacion = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: ALUMNO
# ==========================================
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


# ==========================================
# MODELO: CLASE
# ==========================================
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.DurationField(help_text="Duración de la clase (hh:mm:ss)")
    horario = models.CharField(max_length=50)
    cupo_maximo = models.PositiveIntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="clases")
    alumnos = models.ManyToManyField(Alumno, related_name="clases")

    def __str__(self):
        return self.nombre
