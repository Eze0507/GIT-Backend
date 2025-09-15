from django.urls import path
from . import views

urlpatterns = [
    # CU1: Iniciar sesión
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    
    # CU2: Cerrar sesión
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    
    # CU3: Gestionar Usuario
    path('usuarios/', views.UsuarioListCreateView.as_view(), name='usuario_list_create'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    
    # CU4: Gestionar Roles
    path('roles/', views.RolListCreateView.as_view(), name='rol_list_create'),
    path('roles/<int:pk>/', views.RolDetailView.as_view(), name='rol_detail'),
    
    # CU5: Gestionar Permisos
    path('permisos/', views.PermisoListCreateView.as_view(), name='permiso_list_create'),
    path('permisos/<int:pk>/', views.PermisoDetailView.as_view(), name='permiso_detail'),
    
    # Asignar permisos a roles
    path('rol-permisos/', views.RolPermisoListCreateView.as_view(), name='rol_permiso_list_create'),
    path('rol-permisos/<int:pk>/', views.RolPermisoDetailView.as_view(), name='rol_permiso_detail'),
]
