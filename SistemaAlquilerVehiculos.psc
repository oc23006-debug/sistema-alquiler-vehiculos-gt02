Algoritmo SistemaAlquilerVehiculos
    // Sistema de Alquiler de Vehiculos - Grupo GT02
    // Integrante: Marco Josue Orellana Cortez
    // Entrega 1 - Pseudocodigo
    
    Dimension placas[20], marcas[20], modelos[20], estados[20]
    Definir placas, marcas, modelos, estados Como Cadena
    Definir numVehiculos, opcion, id Como Entero
    
    // Aqui colocamos 5 vehiculos de ejemplo
    numVehiculos <- 5
    placas[1] <- "P123-ABC"; marcas[1] <- "Toyota"; modelos[1] <- "Corolla"; estados[1] <- "Disponible"
    placas[2] <- "P456-DEF"; marcas[2] <- "Honda"; modelos[2] <- "Civic"; estados[2] <- "Alquilado"
    placas[3] <- "P789-GHI"; marcas[3] <- "Nissan"; modelos[3] <- "Sentra"; estados[3] <- "Disponible"
    placas[4] <- "P999-JKL"; marcas[4] <- "Mazda"; modelos[4] <- "3"; estados[4] <- "Mantenimiento"
    placas[5] <- "P111-MNO"; marcas[5] <- "Kia"; modelos[5] <- "Rio"; estados[5] <- "Disponible"
    
    Repetir
        Limpiar Pantalla
        Escribir "====================================="
        Escribir "   SISTEMA DE ALQUILER DE VEHICULOS"
        Escribir "====================================="
        Escribir "1. Ver catalogo"
        Escribir "2. Reservar vehiculo"
        Escribir "3. Devolver vehiculo"
        Escribir "4. Enviar a mantenimiento"
        Escribir "5. Salir"
        Escribir "====================================="
        Escribir "Opcion: "
        Leer opcion
        
        Segun opcion Hacer
            1:
    //            VerCatalogo(placas, marcas, modelos, estados, numVehiculos)
            2:
    //            ReservarVehiculo(placas, marcas, modelos, estados, numVehiculos)
            3:
    //            DevolverVehiculo(placas, marcas, modelos, estados, numVehiculos)
            4:
    //            MantenimientoVehiculo(placas, marcas, modelos, estados, numVehiculos)
            5:
                Escribir "Saliendo..."
            De Otro Modo:
                Escribir "Opcion no valida"
                Esperar Tecla
        FinSegun
    Hasta Que opcion = 5
    
FinAlgoritmo

// ---------------------------------------------------
// MODULO 1: Ver catalogo de vehiculos
// ---------------------------------------------------

SubProceso VerCatalogo(placas, marcas, modelos, estados, numVehiculos)
    Definir i, contDisp, contAlq, contMant Como Entero
    
    contDisp <- 0
    contAlq <- 0
    contMant <- 0
    
    Limpiar Pantalla
    Escribir "========== CATALOGO DE VEHICULOS =========="
    Escribir ""
    Escribir "No. | Placa      | Marca    | Modelo    | Estado"
    Escribir "-----------------------------------------------"
    
    Para i <- 1 Hasta numVehiculos Con Paso 1 Hacer
        Escribir i, "   | ", placas[i], " | ", marcas[i], " | ", modelos[i], " | ", estados[i]
        
        Si estados[i] = "Disponible" Entonces
            contDisp <- contDisp + 1
        Sino
            Si estados[i] = "Alquilado" Entonces
                contAlq <- contAlq + 1
            Sino
                Si estados[i] = "Mantenimiento" Entonces
                    contMant <- contMant + 1
                FinSi
            FinSi
        FinSi
    FinPara
    
    Escribir "-----------------------------------------------"
    Escribir "Resumen - Disponibles: ", contDisp, " | Alquilados: ", contAlq, " | Mantenimiento: ", contMant
    Escribir ""
    Escribir "Presione una tecla..."
    Esperar Tecla
FinSubProceso

// ---------------------------------------------------
// MODULO 2: Reservar un vehiculo
// ---------------------------------------------------

SubProceso ReservarVehiculo(placas, marcas, modelos, estados, numVehiculos)
    Definir id, i Como Entero
    
    Limpiar Pantalla
    Escribir "========== RESERVAR VEHICULO =========="
    Escribir ""
    Escribir "Vehiculos disponibles:"
    Escribir "ID | Placa      | Marca    | Modelo"
    Escribir "---------------------------------"
    
    Para i <- 1 Hasta numVehiculos Con Paso 1 Hacer
        Si estados[i] = "Disponible" Entonces
            Escribir i, "   | ", placas[i], " | ", marcas[i], " | ", modelos[i]
        FinSi
    FinPara
    
    Escribir ""
    Escribir "ID del vehiculo: "
    Leer id
    
    Si id >= 1 Y id <= numVehiculos Entonces
        Si estados[id] = "Disponible" Entonces
            estados[id] <- "Alquilado"
            Escribir ""
            Escribir "RESERVA EXITOSA! Vehiculo ", placas[id], " ahora esta ALQUILADO"
        Sino
            Escribir "ERROR: Vehiculo no disponible. Estado: ", estados[id]
        FinSi
    Sino
        Escribir "ERROR: ID no existe"
    FinSi
    
    Esperar Tecla
FinSubProceso

// ---------------------------------------------------
// MODULO 3: Devolver un vehiculo
// ---------------------------------------------------

SubProceso DevolverVehiculo(placas, marcas, modelos, estados, numVehiculos)
    Definir id, i Como Entero
    
    Limpiar Pantalla
    Escribir "========== DEVOLUCION DE VEHICULO =========="
    Escribir ""
    Escribir "Vehiculos alquilados:"
    Escribir "ID | Placa      | Marca    | Modelo"
    Escribir "-----------------------------------"
    
    Para i <- 1 Hasta numVehiculos Con Paso 1 Hacer
        Si estados[i] = "Alquilado" Entonces
            Escribir i, "   | ", placas[i], " | ", marcas[i], " | ", modelos[i]
        FinSi
    FinPara
    
    Escribir ""
    Escribir "ID del vehiculo a devolver: "
    Leer id
    
    Si id >= 1 Y id <= numVehiculos Entonces
        Si estados[id] = "Alquilado" Entonces
            estados[id] <- "Disponible"
            Escribir ""
            Escribir "DEVOLUCION EXITOSA! Vehiculo ", placas[id], " ahora esta DISPONIBLE"
        Sino
            Escribir "ERROR: Este vehiculo no esta alquilado. Estado: ", estados[id]
        FinSi
    Sino
        Escribir "ERROR: ID no existe"
    FinSi
    
    Esperar Tecla
FinSubProceso