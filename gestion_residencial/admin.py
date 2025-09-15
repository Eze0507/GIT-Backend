from django.contrib import admin
from .models import Propietario, Vivienda, ReconocimientoFacial


@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'documento_identidad', 'telefono', 'activo', 'fecha_registro']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['user__first_name', 'user__last_name', 'documento_identidad', 'telefono']


@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'tipo', 'area', 'habitaciones', 'propietario', 'activa']
    list_filter = ['tipo', 'activa', 'piso']
    search_fields = ['numero', 'propietario__user__first_name', 'propietario__user__last_name']


@admin.register(ReconocimientoFacial)
class ReconocimientoFacialAdmin(admin.ModelAdmin):
    list_display = ['propietario', 'confianza', 'activo', 'fecha_registro']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['propietario__user__first_name', 'propietario__user__last_name']
