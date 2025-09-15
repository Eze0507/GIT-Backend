from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Empleado, Area, Reservacion
from .serializers import EmpleadoSerializer, AreaSerializer, ReservacionSerializer


# CU6: Gestionar Empleado
class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]


class EmpleadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]


# Gestionar Áreas
class AreaListCreateView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]


class AreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]


# Gestionar Reservaciones
class ReservacionListCreateView(generics.ListCreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer
    permission_classes = [IsAuthenticated]


class ReservacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer
    permission_classes = [IsAuthenticated]
