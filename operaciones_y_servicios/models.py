from django.db import models
from django.contrib.auth.models import User


class Empleado(models.Model):
    TIPO_EMPLEADO_CHOICES = [
        ('administrador', 'Administrador'),
        ('portero', 'Portero'),
        ('mantenimiento', 'Mantenimiento'),
        ('limpieza', 'Limpieza'),
        ('seguridad', 'Seguridad'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_empleado = models.CharField(max_length=20, choices=TIPO_EMPLEADO_CHOICES)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    documento_identidad = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.tipo_empleado}"


class Area(models.Model):
    TIPO_AREA_CHOICES = [
        ('recreativa', 'Recreativa'),
        ('deportiva', 'Deportiva'),
        ('social', 'Social'),
        ('comercial', 'Comercial'),
        ('estacionamiento', 'Estacionamiento'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_AREA_CHOICES)
    descripcion = models.TextField(blank=True)
    capacidad_maxima = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=200)
    activa = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"


class Reservacion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reservacion = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return f"Reservación {self.area.nombre} - {self.fecha_reservacion}"
