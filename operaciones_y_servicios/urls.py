from django.urls import path
from . import views

urlpatterns = [
    # CU6: Gestionar Empleado
    path('empleados/', views.EmpleadoListCreateView.as_view(), name='empleado_list_create'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    
    # Gestionar Áreas
    path('areas/', views.AreaListCreateView.as_view(), name='area_list_create'),
    path('areas/<int:pk>/', views.AreaDetailView.as_view(), name='area_detail'),
    
    # Gestionar Reservaciones
    path('reservaciones/', views.ReservacionListCreateView.as_view(), name='reservacion_list_create'),
    path('reservaciones/<int:pk>/', views.ReservacionDetailView.as_view(), name='reservacion_detail'),
]
