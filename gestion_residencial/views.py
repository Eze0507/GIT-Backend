from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Propietario, Vivienda, ReconocimientoFacial
from .serializers import PropietarioSerializer, ViviendaSerializer, ReconocimientoFacialSerializer


# CU9: Gestionar Propietarios
class PropietarioListCreateView(generics.ListCreateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]


class PropietarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]


# Gestionar Viviendas
class ViviendaListCreateView(generics.ListCreateAPIView):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]


class ViviendaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]


# CU19: Reconocimiento facial de residentes (IA)
class ReconocimientoFacialListCreateView(generics.ListCreateAPIView):
    queryset = ReconocimientoFacial.objects.all()
    serializer_class = ReconocimientoFacialSerializer
    permission_classes = [IsAuthenticated]


class ReconocimientoFacialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReconocimientoFacial.objects.all()
    serializer_class = ReconocimientoFacialSerializer
    permission_classes = [IsAuthenticated]
