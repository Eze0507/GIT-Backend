from django.db import models
from django.contrib.auth.models import User


class Cargo(models.Model):
    TIPO_CARGO_CHOICES = [
        ('administracion', 'Administración'),
        ('mantenimiento', 'Mantenimiento'),
        ('seguridad', 'Seguridad'),
        ('limpieza', 'Limpieza'),
        ('porteria', 'Portería'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CARGO_CHOICES)
    descripcion = models.TextField(blank=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"


class Pago(models.Model):
    TIPO_PAGO_CHOICES = [
        ('salario', 'Salario'),
        ('bonificacion', 'Bonificación'),
        ('comision', 'Comisión'),
        ('extra', 'Hora Extra'),
    ]
    
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=20, choices=TIPO_PAGO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    descripcion = models.TextField(blank=True)
    pagado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"Pago {self.empleado.get_full_name()} - {self.fecha_pago}"


class Multa(models.Model):
    TIPO_MULTA_CHOICES = [
        ('ruido', 'Ruido Excesivo'),
        ('basura', 'Manejo Inadecuado de Basura'),
        ('estacionamiento', 'Estacionamiento Incorrecto'),
        ('mascota', 'Mascota Sin Control'),
        ('otro', 'Otro'),
    ]
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada'),
    ]
    
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_multa = models.CharField(max_length=20, choices=TIPO_MULTA_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_multa = models.DateField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Multa"
        verbose_name_plural = "Multas"

    def __str__(self):
        return f"Multa {self.propietario.get_full_name()} - {self.tipo_multa}"
