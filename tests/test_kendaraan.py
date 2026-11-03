import unittest
from models.kendaraan_khusus import Mobil, Bis, Truk

class TestKendaraan(unittest.TestCase):
    
    def test_mobil_tarif(self):
        mobil = Mobil("B1234ABC")
        self.assertEqual(mobil.golongan, 1)
        self.assertEqual(mobil.hitung_tarif(10), 15000)

    def test_bis_tarif(self):
        bis = Bis("D5678XYZ")
        self.assertEqual(bis.golongan, 2)
        self.assertEqual(bis.hitung_tarif(10), 23000)

    def test_truk_tarif(self):
        truk = Truk("L9999ZZ", jumlah_sumbu=3)
        self.assertEqual(truk.golongan, 3)
        self.assertEqual(truk.hitung_tarif(10), 72000)

if __name__ == '__main__':
    unittest.main()