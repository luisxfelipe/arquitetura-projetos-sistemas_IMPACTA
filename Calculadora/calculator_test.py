from calculator import Calculator

import unittest

class TestCalculadora(unittest.TestCase):


    def teste_01_soma(self):
        self.assertEqual(Calculator(2,2).sum(), 4)
        self.assertEqual(Calculator(4,3).sum(), 7)
        self.assertEqual(Calculator(6,4).sum(), 10)

    def teste_02_subtração(self):
        self.assertEqual(Calculator(8,4).subtract(), 4)
        self.assertEqual(Calculator(2,2).subtract(), 0)
        self.assertEqual(Calculator(5,3).subtract(), 2)

    def teste_03_multiplicação(self):
        self.assertEqual(Calculator(2,9).multiplication(), 18)
        self.assertEqual(Calculator(3,5).multiplication(), 15)
        self.assertEqual(Calculator(10,10).multiplication(), 100)

    def teste_04_divisão(self):
        self.assertEqual(Calculator(10,2).division(), 5)
        self.assertEqual(Calculator(30,6).division(), 5)
        self.assertEqual(Calculator(81,9).division(), 9)
        self.assertEqual(Calculator(4,0).division(), 'Não é possivel realizar divisão de um número por 0')
        

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculadora)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()