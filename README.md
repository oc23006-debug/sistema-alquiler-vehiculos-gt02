# Sistema de Alquiler de Vehiculos

## Estado actual
Menu principal con opciones 1 a 5 y 5 vehiculos de ejemplo cargados.

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

## Funciones ya implementadas

### 1. Ver catalogo
Muestra todos los vehiculos con placa, marca, modelo y estado. Al final muestra cuantos hay disponibles, alquilados y en mantenimiento.

### 2. Reservar vehiculo
Lista solo los vehiculos disponibles. Al elegir un ID valido, cambia su estado a "Alquilado".

### 3. Devolver vehiculo
Lista solo los vehiculos alquilados. Al elegir un ID valido, cambia su estado a "Disponible".

## Pendiente
- Opcion 4: Enviar a mantenimiento

## Nota
Ahora si funcionan las opciones que se agragaron recientemente, habia olvidado quitar las "//"

## Como usarlo
El sistema te pide el ID del vehiculo (el numero que ves en la lista). Valida que el ID exista y que el estado sea el correcto para cada accion.
