import ejemplo
import frutasOmarSalgado
import ManuelBuritica
import unittest


'''
creamos los casos de prueba para las funciones
y para eso debemos crear una clase

'''

class Test_ejemplo_suma (unittest.TestCase):
    #Escribimos un metodo:
    def test_suma (self):
        result=ejemplo.suma(7,3)
        self.assertEqual(result,10)

# Despues de este mensaje ustedes deben integrar sus casos de prueba

class TestOmarSalgado (unittest.TestCase):
    #Escribimos un metodo:
    def testFrutas (self):
        result= frutasOmarSalgado.frutas('manzana')
        self.assertEqual(result,1)

class Test_Manuel_Buritica (unittest.TestCase):
    #Escribimos un metodo:
    def testEntrada (self):
        result= ManuelBuritica.entrada(21, 50000)
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()

