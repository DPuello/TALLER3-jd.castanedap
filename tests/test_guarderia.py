import unittest
from guarderia import Guarderia


class TestBoaConstrictor(unittest.TestCase):
    def test_guarderia_alimentar_boa(self):
        guarderia = Guarderia("Guarderia de Hurones", "Calle Falsa 123")
        times = 0
        while times < 10:
            self.assertEqual(guarderia.alimentar_boa(0), "Éxito")
            times += 1
        self.assertEqual(guarderia.alimentar_boa(0), str("La boa está llena"))
        self.assertEqual(guarderia.alimentar_boa(2),
                         str("Esta Boa no existe!"))
