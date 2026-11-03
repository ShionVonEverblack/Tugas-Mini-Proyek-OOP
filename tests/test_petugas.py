import unittest
from models.petugas import Petugas
from models.kendaraan_khusus import Mobil, Bis, Truk

class TestPetugas(unittest.TestCase):
    def setUp(self):
        self.petugas = Petugas("PTG001", "Verity", "Pagi")

    def test_inisialisasi_petugas(self):
        self.assertEqual(self.petugas.id_petugas, "PTG001")
        self.assertEqual(self.petugas.nama, "Verity")
        self.assertEqual(self.petugas.shift, "Pagi")

    def test_validasi_mobil(self):
        mobil = Mobil("B6767ABC")
        self.assertTrue(self.petugas.validasi_kelayakan(mobil))

    def test_validasi_bis(self):
        bis = Bis("D3939XYZ")
        self.assertTrue(self.petugas.validasi_kelayakan(bis))

    def test_validasi_truk(self):
        truk = Truk("Z9999ZZ", jumlah_sumbu=3)
        self.assertTrue(self.petugas.validasi_kelayakan(truk))

    def test_objek_bukan_kendaraan(self):
        self.assertFalse(self.petugas.validasi_kelayakan("B1234ABC"))
        self.assertFalse(self.petugas.validasi_kelayakan(None))

    def test_tampilkan_info(self):
        info = self.petugas.tampilkan_info()

        self.assertIn("PTG001", info)
        self.assertIn("Verity", info)
        self.assertIn("Pagi", info)

if __name__ == "__main__":
    unittest.main()
