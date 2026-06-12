# Sistema de Alquiler de Vehiculos

## Estado actual
Sistema CRUD completo. Menu principal con opciones 1 a 8 y 5 vehiculos de ejemplo cargados. Se agregue la opcion de modificar datos por si el usuario se equivoco al ingresar algo.

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
5. Agregar vehiculo
6. Modificar datos de vehiculo
7. Eliminar vehiculo
8. Salir

## Todas las funciones implementadas (CRUD completo + extras)

### 1. Ver catalogo (Lectura)
Muestra todos los vehiculos con placa, marca, modelo y estado. Al final muestra cuantos hay disponibles, alquilados y en mantenimiento.

### 2. Reservar vehiculo (Actualizacion)
Lista solo los vehiculos disponibles. Al elegir un ID valido, cambia su estado a "Alquilado". Si no hay disponibles te avisa y vuelve al menu.

### 3. Devolver vehiculo (Actualizacion)
Lista solo los vehiculos alquilados. Al elegir un ID valido, cambia su estado a "Disponible". Si no hay alquilados te avisa.

### 4. Enviar a mantenimiento (Actualizacion)
Lista solo los vehiculos disponibles. Al elegir un ID valido, cambia su estado a "Mantenimiento". Solo se pueden mandar a mantenimiento los que estan disponibles.

### 5. Agregar vehiculo (Creacion)
Solicita placa, marca y modelo. Validaciones:
- No puede haber campos vacios
- No puede existir otra placa igual
- Limite maximo de 20 vehiculos
El nuevo vehiculo se agrega con estado "Disponible".

### 6. Modificar datos de vehiculo (Actualizacion avanzada) - NUEVO
Permite cambiar cualquier dato de un vehiculo ya existente. Muestra todos los vehiculos, eliges el ID y luego puedes modificar:
- Placa (valida que no este repetida con otro vehiculo)
- Marca
- Modelo
- Estado (solo permite Disponible, Alquilado o Mantenimiento)
Util para cuando el usuario escribio mal algo o quiere actualizar informacion.

### 7. Eliminar vehiculo (Eliminacion)
Muestra todos los vehiculos. Solicita ID y pide confirmacion antes de eliminar (s/n). Si pones n cancela la operacion.

### 8. Salir
Cierra el sistema con un mensaje.

## Manejo de errores (el sistema no se crashea nunca)
- Si ingresas letras donde va un numero -> te dice "ERROR: Ingrese un numero valido"
- Si pones un ID que no existe -> te dice "ERROR: ID no existe"
- Si intentas reservar un auto que no esta disponible -> te dice cual es su estado actual
- Si dejas un campo vacio al agregar o modificar -> te dice que no puede estar vacio
- Si intentas agregar una placa que ya existe -> te dice "ERROR: Ya existe un vehiculo con esa placa"
- Si llegas al limite de 20 vehiculos -> te dice "ERROR: Capacidad maxima alcanzada"
- Si pones un estado invalido al modificar -> te dice "ERROR: Estado no valido"
- Si no hay vehiculos para reservar/devolver/mantenimiento/eliminar/modificar -> te avisa y vuelve al menu

## Bondades del codigo
- Las listas son paralelas (placas, marcas, modelos, estados) para mantener los datos organizados
- Cada funcion hace una sola cosa (principio de responsabilidad unica)
- Los mensajes de error son claros y no asustan al usuario
- Al final de cada accion pide Enter para continuar, asi puedes leer los resultados
- El resumen del catalogo te dice cuantos autos hay en cada estado
- Capacidad para 20 vehiculos (suficiente para una flota pequena)
- Codigo modular, facil de leer y modificar

## Pruebas unitarias (10 pruebas que verifican todo)

Las pruebas estan en TestAlquilerVehiculos.py. Cada una prueba una funcionalidad especifica.
