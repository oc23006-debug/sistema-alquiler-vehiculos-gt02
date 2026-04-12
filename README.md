# Sistema de Alquiler de Vehiculos

## Estado actual
Sistema completo. Menu principal con opciones 1 a 5 y 5 vehiculos de ejemplo cargados.

## Vehiculos de ejemplo
| # | Placa | Marca | Modelo | Estado |
|---|-------|-------|--------|--------|
| 1 | P123-ABC | Toyota | Corolla | Disponible |
| 2 | P456-DEF | Honda | Civic | Alquilado |
| 3 | P789-GHI | Nissan | Sentra | Disponible |
| 4 | P999-JKL | Mazda | 3 | Mantenimiento |
| 5 | P111-MNO | Kia | Rio | Disponible |

## Opciones del menu
1. Ver catalogo
2. Reservar vehiculo
3. Devolver vehiculo
4. Enviar a mantenimiento
5. Salir

## Todas las funciones implementadas

### 1. Ver catalogo
Muestra todos los vehiculos con placa, marca, modelo y estado. Al final muestra cuantos hay disponibles, alquilados y en mantenimiento.

### 2. Reservar vehiculo
Lista solo los vehiculos disponibles. Al elegir un ID valido, cambia su estado a "Alquilado".

### 3. Devolver vehiculo
Lista solo los vehiculos alquilados. Al elegir un ID valido, cambia su estado a "Disponible".

### 4. Enviar a mantenimiento
Lista solo los vehiculos disponibles. Al elegir un ID valido, cambia su estado a "Mantenimiento".

### 5. Salir
Cierra el sistema.

## Detalles tecnicos
- Capacidad maxima: 20 vehiculos
- Estados posibles: Disponible, Alquilado, Mantenimiento
- Datos guardados en memoria mientras el programa corre
- 5 vehiculos de ejemplo para probar

## Como ejecutar
El pseudocodigo fue escrito en PSeint, puede copiarlo desde el mismo GitHub o puede descargar el archivo .psc y ejecutarlo
