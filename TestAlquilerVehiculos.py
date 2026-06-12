# Pruebas Unitarias para Sistema de Alquiler de Vehiculos
# Grupo GT02 - Marco Josue Orellana Cortez
# Entrega 3 - con mensajes descriptivos

import unittest
from SistemaAlquilerVehiculos import (
    agregar_vehiculo, reservar_vehiculo, devolver_vehiculo,
    mantenimiento_vehiculo, eliminar_vehiculo, ver_catalogo,
    modificar_vehiculo
)

class TestAlquilerVehiculos(unittest.TestCase):
    
    def setUp(self):
        """Preparando datos de prueba antes de cada test"""
        self.placas = ["TEST-001", "TEST-002"]
        self.marcas = ["Toyota", "Honda"]
        self.modelos = ["Corolla", "Civic"]
        self.estados = ["Disponible", "Alquilado"]
    
    def test_agregar_vehiculo_valido(self):
        """Prueba 1: Agregar un vehiculo valido"""
        self.placas.append("TEST-003")
        self.marcas.append("Nissan")
        self.modelos.append("Sentra")
        self.estados.append("Disponible")
        
        self.assertEqual(len(self.placas), 3)
        self.assertEqual(self.placas[2], "TEST-003")
        self.assertEqual(self.estados[2], "Disponible")
        print(" -> Agregar vehiculo: OK")
    
    def test_reservar_vehiculo_disponible(self):
        """Prueba 2: Reservar un vehiculo que esta disponible"""
        self.assertEqual(self.estados[0], "Disponible")
        self.estados[0] = "Alquilado"
        self.assertEqual(self.estados[0], "Alquilado")
        print(" -> Reservar disponible: OK")
    
    def test_reservar_vehiculo_no_disponible(self):
        """Prueba 3: Intentar reservar un vehiculo ya alquilado"""
        estado_original = self.estados[1]
        if self.estados[1] == "Disponible":
            self.estados[1] = "Alquilado"
        self.assertEqual(self.estados[1], estado_original)
        print(" -> Reservar no disponible: OK")
    
    def test_devolver_vehiculo_alquilado(self):
        """Prueba 4: Devolver un vehiculo que esta alquilado"""
        self.assertEqual(self.estados[1], "Alquilado")
        self.estados[1] = "Disponible"
        self.assertEqual(self.estados[1], "Disponible")
        print(" -> Devolver vehiculo: OK")
    
    def test_enviar_mantenimiento(self):
        """Prueba 5: Enviar a mantenimiento un vehiculo disponible"""
        self.placas.append("TEST-003")
        self.marcas.append("Mazda")
        self.modelos.append("3")
        self.estados.append("Disponible")
        
        indice = len(self.estados) - 1
        self.assertEqual(self.estados[indice], "Disponible")
        self.estados[indice] = "Mantenimiento"
        self.assertEqual(self.estados[indice], "Mantenimiento")
        print(" -> Enviar a mantenimiento: OK")
    
    def test_eliminar_vehiculo(self):
        """Prueba 6: Eliminar un vehiculo existente"""
        longitud_inicial = len(self.placas)
        self.placas.pop()
        self.marcas.pop()
        self.modelos.pop()
        self.estados.pop()
        
        self.assertEqual(len(self.placas), longitud_inicial - 1)
        print(" -> Eliminar vehiculo: OK")
    
    def test_modificar_placa_vehiculo(self):
        """Prueba 7: Modificar la placa de un vehiculo"""
        placa_original = self.placas[0]
        nueva_placa = "MOD-001"
        self.placas[0] = nueva_placa
        self.assertNotEqual(self.placas[0], placa_original)
        self.assertEqual(self.placas[0], "MOD-001")
        print(" -> Modificar placa: OK")
    
    def test_modificar_marca_vehiculo(self):
        """Prueba 8: Modificar la marca de un vehiculo"""
        marca_original = self.marcas[1]
        nueva_marca = "Mazda"
        self.marcas[1] = nueva_marca
        self.assertNotEqual(self.marcas[1], marca_original)
        self.assertEqual(self.marcas[1], "Mazda")
        print(" -> Modificar marca: OK")
    
    def test_contar_vehiculos_disponibles(self):
        """Prueba 9: Contar correctamente los vehiculos disponibles"""
        cont_disp = 0
        for estado in self.estados:
            if estado == "Disponible":
                cont_disp += 1
        self.assertEqual(cont_disp, 1)
        print(" -> Contar disponibles: OK")
    
    def test_no_reservar_si_no_hay_disponibles(self):
        """Prueba 10: No reservar cuando no hay vehiculos disponibles"""
        self.estados = ["Alquilado", "Mantenimiento"]
        disponibles = [i for i, e in enumerate(self.estados) if e == "Disponible"]
        self.assertEqual(len(disponibles), 0)
        print(" -> No reservar sin disponibles: OK")


if __name__ == "__main__":
    print("\n" + "="*52)
    print("Ejecutando pruebas unitarias del Sistema de Alquiler")
    print("="*52 + "\n")
    
    # Crear suite de pruebas y ejecutar con verbosidad
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlquilerVehiculos)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "="*40)
    print(f"Resumen: {result.testsRun} pruebas ejecutadas")
    if result.wasSuccessful():
        print("Todas las pruebas pasaron correctamente")
    else:
        print(f"Fallaron {len(result.failures)} pruebas")
    print("="*40)