from django.db import models

class Cita(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100, blank=True)  # puede ser dirección
    fecha = models.DateField()
    hora = models.TimeField()
    uid = models.CharField(max_length=255, unique=True)  # para evitar duplicados
    notas = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    confirmado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"
