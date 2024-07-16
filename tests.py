import unittest
from datetime import datetime
from flask_testing import TestCase
from flask import Flask

from app import app, Cuenta, Operacion, buscar_cuenta

operacion = Operacion("21345", "123", 100, datetime.now().strftime('%d/%m/%Y'))
operacion1 = Operacion("21345", "123", 300, datetime.now().strftime('%d/%m/%Y'))

class TestCuenta(unittest.TestCase):
    def setUp(self):
        # Setting up test data
        self.cuenta1 = Cuenta("21345", "Arnaldo", 200, ["123", "456"])
        self.cuenta2 = Cuenta("123", "Luisa", 400, ["456"])
        self.cuenta3 = Cuenta("456", "Andrea", 300, ["21345"])

    def test_transferir_exito(self):
        # Caso de exito en transferir
        # verificar que
        saldo_inicial_origen = self.cuenta1.saldo
        saldo_inicial_destino = self.cuenta2.saldo
        valor = operacion.valor 
        self.assertTrue(self.cuenta1.transferir(self.cuenta2, valor)[0])
        self.assertEqual(self.cuenta1.saldo, saldo_inicial_origen - valor)
        self.assertEqual(self.cuenta2.saldo, saldo_inicial_destino + valor)

    def test_transferir_saldo_insuficiente(self): # error
        # Caso de error en transferir por saldo insuficiente
        saldo_inicial_origen = self.cuenta1.saldo
        saldo_inicial_destino = self.cuenta2.saldo
        self.assertFalse(self.cuenta1.transferir(self.cuenta2, operacion1.valor)[0])  
        self.assertEqual(self.cuenta1.saldo, saldo_inicial_origen) # saldo debería permanecer igual
        self.assertEqual(self.cuenta2.saldo, saldo_inicial_destino) # saldo debería permanecer igual

    def test_buscar_cuenta_existente(self): # error
        # Caso de éxito en buscar_cuenta
        cuenta_encontrada = buscar_cuenta("21345")

        self.assertEqual(cuenta_encontrada.numero, self.cuenta1.numero)
        self.assertEqual(cuenta_encontrada.nombre, self.cuenta1.nombre)
        self.assertEqual(cuenta_encontrada.saldo, self.cuenta1.saldo)
        self.assertEqual(cuenta_encontrada.contactos, self.cuenta1.contactos)

    def test_buscar_cuenta_no_existente(self):
        # Caso de error en buscar_cuenta no existente
        self.assertIsNone(buscar_cuenta("99999"))

    def test_transferir_destino_no_en_contactos(self):
        # caso de error de un test para verificar que la persona destino no esta en la lista de contactos
        saldo_inicial_origen = self.cuenta1.saldo
        self.assertFalse(self.cuenta2.transferir(self.cuenta1, operacion.valor)[0])
        self.assertEqual(self.cuenta1.saldo, saldo_inicial_origen)

class TestOperacion(unittest.TestCase):
    def setUp(self):
        # preparar datos de prueba
        self.operacion = Operacion("21345", "123", 100, datetime.now().strftime('%d/%m/%Y'))

    def test_operacion_atributos(self):
        # Verificar que los atributos de la operación se inicializan correctamente
        self.assertEqual(self.operacion.origen, "21345")
        self.assertEqual(self.operacion.destino, "123")
        self.assertEqual(self.operacion.valor, 100)
        self.assertIsInstance(datetime.strptime(self.operacion.fecha, '%d/%m/%Y'), datetime)

if __name__ == '__main__':
    unittest.main()
