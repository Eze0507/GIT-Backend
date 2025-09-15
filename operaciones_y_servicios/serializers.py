from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Empleado, Area, Reservacion


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']


class EmpleadoSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Empleado
        fields = [
            'id', 'user', 'tipo_empleado', 'telefono', 'direccion',
            'documento_identidad', 'fecha_nacimiento', 'fecha_ingreso',
            'salario', 'activo', 'fecha_registro', 'fecha_actualizacion',
            'nombre_completo'
        ]
    
    def get_nombre_completo(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id', 'nombre', 'tipo', 'descripcion', 'capacidad_maxima',
            'ubicacion', 'activa', 'fecha_registro'
        ]


class ReservacionSerializer(serializers.ModelSerializer):
    area_nombre = serializers.CharField(source='area.nombre', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.get_full_name', read_only=True)
    
    class Meta:
        model = Reservacion
        fields = [
            'id', 'area', 'area_nombre', 'usuario', 'usuario_nombre',
            'fecha_reservacion', 'hora_inicio', 'hora_fin', 'motivo',
            'estado', 'fecha_creacion', 'fecha_actualizacion'
        ]
