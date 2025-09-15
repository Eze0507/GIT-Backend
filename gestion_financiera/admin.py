from django.contrib import admin
from .models import Cargo, Pago, Multa


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'salario_base', 'activo', 'fecha_creacion']
    list_filter = ['tipo', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'cargo', 'tipo_pago', 'monto', 'fecha_pago', 'pagado']
    list_filter = ['tipo_pago', 'pagado', 'fecha_pago']
    search_fields = ['empleado__first_name', 'empleado__last_name', 'cargo__nombre']


@admin.register(Multa)
class MultaAdmin(admin.ModelAdmin):
    list_display = ['propietario', 'tipo_multa', 'monto', 'fecha_multa', 'estado']
    list_filter = ['tipo_multa', 'estado', 'fecha_multa']
    search_fields = ['propietario__first_name', 'propietario__last_name', 'descripcion']
