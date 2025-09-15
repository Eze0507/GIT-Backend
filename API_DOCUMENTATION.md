# API de Gestión de Condominios

Esta API está desarrollada con Django REST Framework y maneja 4 paquetes principales del sistema de condominios.

## Estructura del Proyecto

### Paquetes Implementados:

1. **Seguridad y Accesos** (`/api/seguridad/`)
2. **Gestión Residencial** (`/api/residencial/`)
3. **Operaciones y Servicios** (`/api/operaciones/`)
4. **Gestión Financiera** (`/api/financiera/`)

## Casos de Uso Implementados

### Seguridad y Accesos
- **CU1**: Iniciar sesión - `POST /api/seguridad/login/`
- **CU2**: Cerrar sesión - `POST /api/seguridad/logout/`
- **CU3**: Gestionar Usuario - `GET/POST /api/seguridad/usuarios/`
- **CU4**: Gestionar Roles - `GET/POST /api/seguridad/roles/`
- **CU5**: Gestionar Permisos - `GET/POST /api/seguridad/permisos/`

### Gestión Residencial
- **CU9**: Gestionar Propietarios - `GET/POST /api/residencial/propietarios/`
- **CU19**: Reconocimiento facial de residentes (IA) - `GET/POST /api/residencial/reconocimiento-facial/`

### Operaciones y Servicios
- **CU6**: Gestionar Empleado - `GET/POST /api/operaciones/empleados/`

### Gestión Financiera
- **CU7**: Gestionar Cargos - `GET/POST /api/financiera/cargos/`

## Endpoints Disponibles

### Seguridad y Accesos (`/api/seguridad/`)

#### Autenticación
- `POST /login/` - Iniciar sesión
- `POST /logout/` - Cerrar sesión

#### Usuarios
- `GET /usuarios/` - Listar usuarios
- `POST /usuarios/` - Crear usuario
- `GET /usuarios/{id}/` - Obtener usuario
- `PUT /usuarios/{id}/` - Actualizar usuario
- `DELETE /usuarios/{id}/` - Eliminar usuario

#### Roles
- `GET /roles/` - Listar roles
- `POST /roles/` - Crear rol
- `GET /roles/{id}/` - Obtener rol
- `PUT /roles/{id}/` - Actualizar rol
- `DELETE /roles/{id}/` - Eliminar rol

#### Permisos
- `GET /permisos/` - Listar permisos
- `POST /permisos/` - Crear permiso
- `GET /permisos/{id}/` - Obtener permiso
- `PUT /permisos/{id}/` - Actualizar permiso
- `DELETE /permisos/{id}/` - Eliminar permiso

#### Asignación de Permisos a Roles
- `GET /rol-permisos/` - Listar asignaciones
- `POST /rol-permisos/` - Asignar permiso a rol
- `GET /rol-permisos/{id}/` - Obtener asignación
- `PUT /rol-permisos/{id}/` - Actualizar asignación
- `DELETE /rol-permisos/{id}/` - Eliminar asignación

### Gestión Residencial (`/api/residencial/`)

#### Propietarios
- `GET /propietarios/` - Listar propietarios
- `POST /propietarios/` - Crear propietario
- `GET /propietarios/{id}/` - Obtener propietario
- `PUT /propietarios/{id}/` - Actualizar propietario
- `DELETE /propietarios/{id}/` - Eliminar propietario

#### Viviendas
- `GET /viviendas/` - Listar viviendas
- `POST /viviendas/` - Crear vivienda
- `GET /viviendas/{id}/` - Obtener vivienda
- `PUT /viviendas/{id}/` - Actualizar vivienda
- `DELETE /viviendas/{id}/` - Eliminar vivienda

#### Reconocimiento Facial
- `GET /reconocimiento-facial/` - Listar reconocimientos
- `POST /reconocimiento-facial/` - Crear reconocimiento
- `GET /reconocimiento-facial/{id}/` - Obtener reconocimiento
- `PUT /reconocimiento-facial/{id}/` - Actualizar reconocimiento
- `DELETE /reconocimiento-facial/{id}/` - Eliminar reconocimiento

### Operaciones y Servicios (`/api/operaciones/`)

#### Empleados
- `GET /empleados/` - Listar empleados
- `POST /empleados/` - Crear empleado
- `GET /empleados/{id}/` - Obtener empleado
- `PUT /empleados/{id}/` - Actualizar empleado
- `DELETE /empleados/{id}/` - Eliminar empleado

#### Áreas
- `GET /areas/` - Listar áreas
- `POST /areas/` - Crear área
- `GET /areas/{id}/` - Obtener área
- `PUT /areas/{id}/` - Actualizar área
- `DELETE /areas/{id}/` - Eliminar área

#### Reservaciones
- `GET /reservaciones/` - Listar reservaciones
- `POST /reservaciones/` - Crear reservación
- `GET /reservaciones/{id}/` - Obtener reservación
- `PUT /reservaciones/{id}/` - Actualizar reservación
- `DELETE /reservaciones/{id}/` - Eliminar reservación

### Gestión Financiera (`/api/financiera/`)

#### Cargos
- `GET /cargos/` - Listar cargos
- `POST /cargos/` - Crear cargo
- `GET /cargos/{id}/` - Obtener cargo
- `PUT /cargos/{id}/` - Actualizar cargo
- `DELETE /cargos/{id}/` - Eliminar cargo

#### Pagos
- `GET /pagos/` - Listar pagos
- `POST /pagos/` - Crear pago
- `GET /pagos/{id}/` - Obtener pago
- `PUT /pagos/{id}/` - Actualizar pago
- `DELETE /pagos/{id}/` - Eliminar pago

#### Multas
- `GET /multas/` - Listar multas
- `POST /multas/` - Crear multa
- `GET /multas/{id}/` - Obtener multa
- `PUT /multas/{id}/` - Actualizar multa
- `DELETE /multas/{id}/` - Eliminar multa

## Autenticación

La API utiliza autenticación por token. Para obtener un token:

1. Hacer POST a `/api/seguridad/login/` con username y password
2. Usar el token devuelto en el header `Authorization: Token <token>`

### Ejemplo de Login:
```json
POST /api/seguridad/login/
{
    "username": "admin",
    "password": "admin123"
}
```

### Respuesta:
```json
{
    "token": "abc123...",
    "user_id": 1,
    "username": "admin",
    "message": "Sesión iniciada correctamente"
}
```

## Instalación y Configuración

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Aplicar migraciones:
```bash
python manage.py migrate
```

3. Crear superusuario:
```bash
python manage.py createsuperuser
```

4. Ejecutar servidor:
```bash
python manage.py runserver
```

## Credenciales por Defecto

- **Usuario**: admin
- **Contraseña**: admin123

## Características Técnicas

- **Framework**: Django 5.2.6 + Django REST Framework 3.15.2
- **Base de datos**: SQLite (desarrollo)
- **Autenticación**: Token Authentication
- **Paginación**: 20 elementos por página
- **CORS**: Habilitado para desarrollo

## Modelos Principales

### Seguridad y Accesos
- `Rol`: Roles del sistema
- `Permiso`: Permisos específicos
- `RolPermiso`: Asignación de permisos a roles
- `UsuarioPersonalizado`: Extensión del usuario de Django

### Gestión Residencial
- `Propietario`: Propietarios de viviendas
- `Vivienda`: Viviendas del condominio
- `ReconocimientoFacial`: Datos de reconocimiento facial

### Operaciones y Servicios
- `Empleado`: Empleados del condominio
- `Area`: Áreas comunes
- `Reservacion`: Reservaciones de áreas

### Gestión Financiera
- `Cargo`: Cargos de empleados
- `Pago`: Pagos a empleados
- `Multa`: Multas a propietarios
