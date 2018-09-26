import ejemplo
import frutasOmarSalgado
import ManuelBuritica
import SEBASTIAN_YEPES
import factorialDiegoHerrera
import JOHAN_ALVAREZ
import JOHAN_LOPEZ
import Andres_Suarez
import KarinaBolivar
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

#Despues de este mensaje ustedes deben integrar sus casos de prueba

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

class Test_ejemplo_sebastian (unittest.TestCase):
    #Escribimos un metodo:
    def test_par_impar (self):
        result=SEBASTIAN_YEPES.par_impares(2)
        self.assertEqual(result,1)
        
class testDiegoHerrera (unittest.TestCase):
    #Escribimos un metodo:
    def testfactorial(self):
        result= factorialDiegoHerrera.fact(4)
        self.assertEqual(result,24)

#clase Johan Alvarez
class Test_ejemplo_triangulo (unittest.TestCase):
    #Escribimos un metodo:
    def test_area_triangulo (self):
        result=JOHAN_ALVAREZ.area_triangulo(2,2)
        self.assertEqual(result,2)

#clase Johan Lopez
class Test_ejemplo_calcular (unittest.TestCase):
    #Escribimos un metodo:
    def test_calcular (self):
        result=JOHAN_LOPEZ.calcular(2000,2000)
        self.assertEqual(result,-38000)

class Test_Andres_Suarez (unittest.TestCase):
    #Escribimos un metodo:
    def testPromedio (self):
        result= Andres_Suarez.promedio(5,4.5,3.5,1)
        self.assertEqual(result,3.5)

class TestKarinaBolivar (unittest.TestCase):
    #Escribimos un metodo:
    def testMascotas (self):
        result= KarinaBolivar.mascotas('pinto')
        self.assertEqual(result,1)        

if __name__ == '__main__':
    unittest.main()
    

