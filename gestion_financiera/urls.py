from django.urls import path
from . import views

urlpatterns = [
    # CU7: Gestionar Cargos
    path('cargos/', views.CargoListCreateView.as_view(), name='cargo_list_create'),
    path('cargos/<int:pk>/', views.CargoDetailView.as_view(), name='cargo_detail'),
    
    # Gestionar Pagos
    path('pagos/', views.PagoListCreateView.as_view(), name='pago_list_create'),
    path('pagos/<int:pk>/', views.PagoDetailView.as_view(), name='pago_detail'),
    
    # Gestionar Multas
    path('multas/', views.MultaListCreateView.as_view(), name='multa_list_create'),
    path('multas/<int:pk>/', views.MultaDetailView.as_view(), name='multa_detail'),
]
