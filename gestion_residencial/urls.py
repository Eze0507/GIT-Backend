from django.urls import path
from . import views

urlpatterns = [
    # CU9: Gestionar Propietarios
    path('propietarios/', views.PropietarioListCreateView.as_view(), name='propietario_list_create'),
    path('propietarios/<int:pk>/', views.PropietarioDetailView.as_view(), name='propietario_detail'),
    
    # Gestionar Viviendas
    path('viviendas/', views.ViviendaListCreateView.as_view(), name='vivienda_list_create'),
    path('viviendas/<int:pk>/', views.ViviendaDetailView.as_view(), name='vivienda_detail'),
    
    # CU19: Reconocimiento facial de residentes (IA)
    path('reconocimiento-facial/', views.ReconocimientoFacialListCreateView.as_view(), name='reconocimiento_facial_list_create'),
    path('reconocimiento-facial/<int:pk>/', views.ReconocimientoFacialDetailView.as_view(), name='reconocimiento_facial_detail'),
]
