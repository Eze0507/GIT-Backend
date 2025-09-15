from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Propietario, Vivienda, ReconocimientoFacial


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']


class PropietarioSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Propietario
        fields = [
            'id', 'user', 'telefono', 'direccion', 'documento_identidad',
            'fecha_nacimiento', 'activo', 'fecha_registro', 'fecha_actualizacion',
            'nombre_completo'
        ]
    
    def get_nombre_completo(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class ViviendaSerializer(serializers.ModelSerializer):
    propietario_nombre = serializers.CharField(source='propietario.user.get_full_name', read_only=True)
    
    class Meta:
        model = Vivienda
        fields = [
            'id', 'numero', 'tipo', 'area', 'habitaciones', 'banos',
            'piso', 'propietario', 'propietario_nombre', 'activa', 'fecha_registro'
        ]


class ReconocimientoFacialSerializer(serializers.ModelSerializer):
    propietario_nombre = serializers.CharField(source='propietario.user.get_full_name', read_only=True)
    
    class Meta:
        model = ReconocimientoFacial
        fields = [
            'id', 'propietario', 'propietario_nombre', 'imagen_rostro',
            'vector_caracteristicas', 'confianza', 'activo', 'fecha_registro',
            'fecha_actualizacion'
        ]
