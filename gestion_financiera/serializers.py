from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cargo, Pago, Multa


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = [
            'id', 'nombre', 'tipo', 'descripcion', 'salario_base',
            'activo', 'fecha_creacion', 'fecha_actualizacion'
        ]


class PagoSerializer(serializers.ModelSerializer):
    empleado_nombre = serializers.CharField(source='empleado.get_full_name', read_only=True)
    cargo_nombre = serializers.CharField(source='cargo.nombre', read_only=True)
    
    class Meta:
        model = Pago
        fields = [
            'id', 'empleado', 'empleado_nombre', 'cargo', 'cargo_nombre',
            'tipo_pago', 'monto', 'fecha_pago', 'periodo_inicio', 'periodo_fin',
            'descripcion', 'pagado', 'fecha_creacion'
        ]


class MultaSerializer(serializers.ModelSerializer):
    propietario_nombre = serializers.CharField(source='propietario.get_full_name', read_only=True)
    
    class Meta:
        model = Multa
        fields = [
            'id', 'propietario', 'propietario_nombre', 'tipo_multa', 'monto',
            'descripcion', 'fecha_multa', 'fecha_vencimiento', 'estado',
            'fecha_pago', 'fecha_creacion', 'fecha_actualizacion'
        ]
