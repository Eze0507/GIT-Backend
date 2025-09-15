from django.contrib import admin
from .models import Rol, Permiso, RolPermiso, UsuarioPersonalizado


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']


@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'codigo', 'descripcion']


@admin.register(RolPermiso)
class RolPermisoAdmin(admin.ModelAdmin):
    list_display = ['rol', 'permiso', 'fecha_asignacion']
    list_filter = ['fecha_asignacion']
    search_fields = ['rol__nombre', 'permiso__nombre']


@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ['user', 'rol', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'rol', 'fecha_creacion']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
