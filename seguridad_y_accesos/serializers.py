from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rol, Permiso, RolPermiso, UsuarioPersonalizado


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ['id', 'nombre', 'descripcion', 'codigo', 'activo', 'fecha_creacion']


class RolSerializer(serializers.ModelSerializer):
    permisos = PermisoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion', 'permisos']


class RolPermisoSerializer(serializers.ModelSerializer):
    rol_nombre = serializers.CharField(source='rol.nombre', read_only=True)
    permiso_nombre = serializers.CharField(source='permiso.nombre', read_only=True)
    
    class Meta:
        model = RolPermiso
        fields = ['id', 'rol', 'permiso', 'rol_nombre', 'permiso_nombre', 'fecha_asignacion']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']


class UsuarioPersonalizadoSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    rol_nombre = serializers.CharField(source='rol.nombre', read_only=True)
    
    class Meta:
        model = UsuarioPersonalizado
        fields = ['id', 'user', 'rol', 'rol_nombre', 'telefono', 'direccion', 'activo', 'fecha_creacion', 'fecha_actualizacion']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
