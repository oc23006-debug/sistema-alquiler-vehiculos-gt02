# Sistema de Alquiler de Vehiculos - Grupo GT02
# Integrante: Marco Josue Orellana Cortez
# Entrega 2 - Python - Parte 3 (Actualizacion)

def ver_catalogo(placas, marcas, modelos, estados):
    cont_disp = 0
    cont_alq = 0
    cont_mant = 0
    
    print("\n========== CATALOGO DE VEHICULOS ==========")
    print("")
    print("No. | Placa      | Marca    | Modelo    | Estado")
    print("-----------------------------------------------")
    
    for i in range(len(placas)):
        print(f"{i+1}   | {placas[i]} | {marcas[i]} | {modelos[i]} | {estados[i]}")
        
        if estados[i] == "Disponible":
            cont_disp += 1
        elif estados[i] == "Alquilado":
            cont_alq += 1
        elif estados[i] == "Mantenimiento":
            cont_mant += 1
    
    print("-----------------------------------------------")
    print(f"Resumen - Disponibles: {cont_disp} | Alquilados: {cont_alq} | Mantenimiento: {cont_mant}")
    print("")
    input("Presione Enter para continuar...")

def agregar_vehiculo(placas, marcas, modelos, estados):
    print("\n========== AGREGAR VEHICULO ==========")
    print("")
    
    if len(placas) >= 20:
        print("ERROR: Capacidad maxima alcanzada (20 vehiculos)")
        input("Presione Enter para continuar...")
        return
    
    nueva_placa = input("Placa (formato P123-ABC): ")
    nueva_marca = input("Marca: ")
    nuevo_modelo = input("Modelo: ")
    
    for placa in placas:
        if placa.upper() == nueva_placa.upper():
            print("ERROR: Ya existe un vehiculo con esa placa")
            input("Presione Enter para continuar...")
            return
    
    placas.append(nueva_placa)
    marcas.append(nueva_marca)
    modelos.append(nuevo_modelo)
    estados.append("Disponible")
    
    print(f"\nVEHICULO AGREGADO EXITOSAMENTE! {nueva_placa} - {nueva_marca} {nuevo_modelo}")
    input("Presione Enter para continuar...")

def reservar_vehiculo(placas, marcas, modelos, estados):
    print("\n========== RESERVAR VEHICULO ==========")
    print("")
    print("Vehiculos disponibles:")
    print("ID | Placa      | Marca    | Modelo")
    print("---------------------------------")
    
    disponibles = []
    for i in range(len(estados)):
        if estados[i] == "Disponible":
            print(f"{i+1}   | {placas[i]} | {marcas[i]} | {modelos[i]}")
            disponibles.append(i)
    
    if len(disponibles) == 0:
        print("No hay vehiculos disponibles")
        input("Presione Enter para continuar...")
        return
    
    try:
        id_vehiculo = int(input("\nID del vehiculo: ")) - 1
        if 0 <= id_vehiculo < len(estados):
            if estados[id_vehiculo] == "Disponible":
                estados[id_vehiculo] = "Alquilado"
                print(f"\nRESERVA EXITOSA! Vehiculo {placas[id_vehiculo]} ahora esta ALQUILADO")
            else:
                print(f"ERROR: Vehiculo no disponible. Estado: {estados[id_vehiculo]}")
        else:
            print("ERROR: ID no existe")
    except ValueError:
        print("ERROR: Ingrese un numero valido")
    
    input("\nPresione Enter para continuar...")

def devolver_vehiculo(placas, marcas, modelos, estados):
    print("\n========== DEVOLUCION DE VEHICULO ==========")
    print("")
    print("Vehiculos alquilados:")
    print("ID | Placa      | Marca    | Modelo")
    print("-----------------------------------")
    
    alquilados = []
    for i in range(len(estados)):
        if estados[i] == "Alquilado":
            print(f"{i+1}   | {placas[i]} | {marcas[i]} | {modelos[i]}")
            alquilados.append(i)
    
    if len(alquilados) == 0:
        print("No hay vehiculos alquilados")
        input("Presione Enter para continuar...")
        return
    
    try:
        id_vehiculo = int(input("\nID del vehiculo a devolver: ")) - 1
        if 0 <= id_vehiculo < len(estados):
            if estados[id_vehiculo] == "Alquilado":
                estados[id_vehiculo] = "Disponible"
                print(f"\nDEVOLUCION EXITOSA! Vehiculo {placas[id_vehiculo]} ahora esta DISPONIBLE")
            else:
                print(f"ERROR: Este vehiculo no esta alquilado. Estado: {estados[id_vehiculo]}")
        else:
            print("ERROR: ID no existe")
    except ValueError:
        print("ERROR: Ingrese un numero valido")
    
    input("\nPresione Enter para continuar...")

def mantenimiento_vehiculo(placas, marcas, modelos, estados):
    print("\n========== ENVIAR A MANTENIMIENTO ==========")
    print("")
    print("Vehiculos disponibles:")
    print("ID | Placa      | Marca    | Modelo")
    print("----------------------------------------")
    
    disponibles = []
    for i in range(len(estados)):
        if estados[i] == "Disponible":
            print(f"{i+1}   | {placas[i]} | {marcas[i]} | {modelos[i]}")
            disponibles.append(i)
    
    if len(disponibles) == 0:
        print("No hay vehiculos disponibles para enviar a mantenimiento")
        input("Presione Enter para continuar...")
        return
    
    try:
        id_vehiculo = int(input("\nID del vehiculo: ")) - 1
        if 0 <= id_vehiculo < len(estados):
            if estados[id_vehiculo] == "Disponible":
                estados[id_vehiculo] = "Mantenimiento"
                print(f"\nVEHICULO ENVIADO A MANTENIMIENTO! {placas[id_vehiculo]} ahora esta EN MANTENIMIENTO")
            else:
                print(f"ERROR: Solo vehiculos DISPONIBLES van a mantenimiento. Estado: {estados[id_vehiculo]}")
        else:
            print("ERROR: ID no existe")
    except ValueError:
        print("ERROR: Ingrese un numero valido")
    
    input("\nPresione Enter para continuar...")

def main():
    placas = ["P123-ABC", "P456-DEF", "P789-GHI", "P999-JKL", "P111-MNO"]
    marcas = ["Toyota", "Honda", "Nissan", "Mazda", "Kia"]
    modelos = ["Corolla", "Civic", "Sentra", "3", "Rio"]
    estados = ["Disponible", "Alquilado", "Disponible", "Mantenimiento", "Disponible"]
    
    while True:
        print("\n=====================================")
        print("   SISTEMA DE ALQUILER DE VEHICULOS")
        print("=====================================")
        print("1. Ver catalogo")
        print("2. Reservar vehiculo")
        print("3. Devolver vehiculo")
        print("4. Enviar a mantenimiento")
        print("5. Agregar vehiculo")
        print("6. Eliminar vehiculo")
        print("7. Salir")
        print("=====================================")
        opcion = input("Opcion: ")
        
        if opcion == "1":
            ver_catalogo(placas, marcas, modelos, estados)
        elif opcion == "2":
            reservar_vehiculo(placas, marcas, modelos, estados)
        elif opcion == "3":
            devolver_vehiculo(placas, marcas, modelos, estados)
        elif opcion == "4":
            mantenimiento_vehiculo(placas, marcas, modelos, estados)
        elif opcion == "5":
            agregar_vehiculo(placas, marcas, modelos, estados)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida o no implementada aun")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()