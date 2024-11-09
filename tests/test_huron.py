import unittest
from huron import Huron


class TestHuron(unittest.TestCase):
    def test_huron_hacer_sonido(self):
        huron = Huron("Bobby", 2, 9.1, "Canada", 2)
        huron2 = Huron("Nemo", 5, 3.6, "Colombia", 15.2)
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")
        self.assertEqual(huron2.hacer_sonido(), "¡Eek Eek!")

    def test_huron_calcular_flete(self):
        huron = Huron("Bobby", 2, 9.1, "Canada", 2)
        huron2 = Huron("Nemo", 5, 3.6, "Colombia", 15.2)
        self.assertEqual(huron.calcular_flete(), 18.2)
        self.assertEqual(huron2.calcular_flete(), 54.72)
