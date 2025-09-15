from django.db import models
from django.contrib.auth.models import User


class Propietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    documento_identidad = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Vivienda(models.Model):
    TIPO_VIVIENDA_CHOICES = [
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
        ('duplex', 'Dúplex'),
        ('penthouse', 'Penthouse'),
    ]
    
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_VIVIENDA_CHOICES)
    area = models.DecimalField(max_digits=8, decimal_places=2)
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField()
    piso = models.PositiveIntegerField(null=True, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True, blank=True)
    activa = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"

    def __str__(self):
        return f"Vivienda {self.numero}"


class ReconocimientoFacial(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    imagen_rostro = models.ImageField(upload_to='reconocimiento_facial/')
    vector_caracteristicas = models.TextField()  # Almacena el vector de características faciales
    confianza = models.FloatField()  # Nivel de confianza del reconocimiento
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reconocimiento Facial"
        verbose_name_plural = "Reconocimientos Faciales"

    def __str__(self):
        return f"Reconocimiento - {self.propietario.user.first_name} {self.propietario.user.last_name}"
