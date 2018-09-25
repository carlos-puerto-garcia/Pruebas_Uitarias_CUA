import ejemplo
import frutasOmarSalgado
import ManuelBuritica
import SEBASTIAN_YEPES
import factorialDiegoHerrera
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



#clase sebastian yepes pares e impares:

class Test_ejemplo_sebastian (unittest.TestCase):
    
    def test_par_impar (self):
        result=SEBASTIAN_YEPES.par_impares(2)
        self.assertEqual(result,1)

        
class testDiegoHerrera (unittest.TestCase):
    #Escribimos un metodo:
    def testfactorial(self):
        result= factorialDiegoHerrera.fact(4)
        self.assertEqual(result,24)
        
if __name__ == '__main__':
    unittest.main()
    

