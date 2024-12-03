import unittest
from clases.calculadora  import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(3, 5), 8)
        self.assertEqual(self.calc.sumar(-2, 5), 3)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 5), 5)
        self.assertEqual(self.calc.restar(0, 7), -7)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 5), 20)
        self.assertEqual(self.calc.multiplicar(-3, 5), -15)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(7, -1), -7)
        self.assertEqual(self.calc.dividir(0, 5), 0)
        self.assertEqual(self.calc.dividir(5, 0), "Error: No se puede dividir entre cero.")

if __name__ == "__main__":
    unittest.main()
