# Modul yang akan diuji
def pangkat_dua(angka):
    return angka ** 2

# Modul pengujian (unit test)
import unittest

class TestPangkatDua(unittest.TestCase):

    def test_pangkat_dua_dengan_angka_positif(self):
        self.assertEqual(pangkat_dua(4), 16)
        self.assertEqual(pangkat_dua(5), 25)

    def test_pangkat_dua_dengan_angka_negatif(self):
        self.assertEqual(pangkat_dua(-3), 9)
        self.assertEqual(pangkat_dua(-6), 36)

    def test_pangkat_dua_dengan_nol(self):
        self.assertEqual(pangkat_dua(0), 0)

if __name__ == '__main__':
    unittest.main()
