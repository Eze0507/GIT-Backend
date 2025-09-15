from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cargo, Pago, Multa
from .serializers import CargoSerializer, PagoSerializer, MultaSerializer


# CU7: Gestionar Cargos
class CargoListCreateView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]


class CargoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]


# Gestionar Pagos
class PagoListCreateView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]


class PagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]


# Gestionar Multas
class MultaListCreateView(generics.ListCreateAPIView):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer
    permission_classes = [IsAuthenticated]


class MultaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer
    permission_classes = [IsAuthenticated]
