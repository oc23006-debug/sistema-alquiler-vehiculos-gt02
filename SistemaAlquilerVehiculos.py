# Sistema de Alquiler de Vehiculos - Grupo GT02
# Integrante: Marco Josue Orellana Cortez
# Entrega 2 - Python - Parte 2 (Lectura y Creacion)

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
    
    # Verificar si la placa ya existe
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