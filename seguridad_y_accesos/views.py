from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Rol, Permiso, RolPermiso, UsuarioPersonalizado
from .serializers import (
    RolSerializer, PermisoSerializer, RolPermisoSerializer,
    UsuarioPersonalizadoSerializer, LoginSerializer
)


# CU1: Iniciar sesión
@api_view(['POST'])
@permission_classes([AllowAny])
def iniciar_sesion(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'message': 'Sesión iniciada correctamente'
            })
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CU2: Cerrar sesión
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cerrar_sesion(request):
    try:
        request.user.auth_token.delete()
    except:
        pass
    logout(request)
    return Response({'message': 'Sesión cerrada correctamente'})


# CU3: Gestionar Usuario
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioPersonalizadoSerializer
    permission_classes = [IsAuthenticated]


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioPersonalizadoSerializer
    permission_classes = [IsAuthenticated]


# CU4: Gestionar Roles
class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]


class RolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]


# CU5: Gestionar Permisos
class PermisoListCreateView(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]


class PermisoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]


class RolPermisoListCreateView(generics.ListCreateAPIView):
    queryset = RolPermiso.objects.all()
    serializer_class = RolPermisoSerializer
    permission_classes = [IsAuthenticated]


class RolPermisoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RolPermiso.objects.all()
    serializer_class = RolPermisoSerializer
    permission_classes = [IsAuthenticated]
