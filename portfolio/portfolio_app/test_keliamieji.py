import unittest
from keliamieji_metai import ar_keliamieji

class KeliamiejiTest(unittest.TestCase):

    def test_ar_keliamieji(self):
        rezultatas = ar_keliamieji(2020)
        lukestis = "Keliamieji"
        self.assertEqual(lukestis, rezultatas)