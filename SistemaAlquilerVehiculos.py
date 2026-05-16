# Sistema de Alquiler de Vehiculos - Grupo GT02
# Integrante: Marco Josue Orellana Cortez
# Entrega 2 - Python - Parte 1 (Estructura base)

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
        
        if opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida o no implementada aun")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()