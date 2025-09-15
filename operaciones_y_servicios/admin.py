from django.contrib import admin
from .models import Empleado, Area, Reservacion


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['user', 'tipo_empleado', 'documento_identidad', 'salario', 'activo', 'fecha_ingreso']
    list_filter = ['tipo_empleado', 'activo', 'fecha_ingreso']
    search_fields = ['user__first_name', 'user__last_name', 'documento_identidad', 'telefono']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'capacidad_maxima', 'ubicacion', 'activa']
    list_filter = ['tipo', 'activa']
    search_fields = ['nombre', 'descripcion', 'ubicacion']


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ['area', 'usuario', 'fecha_reservacion', 'hora_inicio', 'estado']
    list_filter = ['estado', 'fecha_reservacion', 'area__tipo']
    search_fields = ['area__nombre', 'usuario__first_name', 'usuario__last_name', 'motivo']
