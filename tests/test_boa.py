import unittest
from boa_constrictor import BoaConstrictor


class TestBoaConstrictor(unittest.TestCase):
    def test_boa_constrictor_hacer_sonido(self):
        boa = BoaConstrictor("Sneaky", 5, 3.6, "Colombia", 15.2)
        boa2 = BoaConstrictor("Kenny", 2, 9.1, "Canada", 2)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")
        self.assertEqual(boa2.hacer_sonido(), "¡Tsss!")

    def test_boa_constrictor_calcular_flete(self):
        boa = BoaConstrictor("Sneaky", 5, 3.6, "Colombia", 15.2)
        boa2 = BoaConstrictor("Kenny", 2, 9.1, "Canada", 2)
        self.assertEqual(boa.calcular_flete(), 54.72)
        self.assertEqual(boa2.calcular_flete(), 18.2)

    def test_boa_constrictor_comer_raton(self):
        boa = BoaConstrictor("Sneaky", 5, 3.6, "Colombia", 15.2)
        times = 0
        while times < 10:
            boa.comer_raton()
            times += 1
            self.assertEqual(boa.ratones_comidos, times)
        self.assertEqual(str(boa.comer_raton()), "Demasiados Ratones!")
