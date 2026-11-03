import unittest
from models.gerbang_tol import GerbangTol
from models.petugas import Petugas
from models.kendaraan_khusus import Mobil, Bis, Truk

class TestGerbangTol(unittest.TestCase):
    def setUp(self):
        self.petugas = Petugas("PTG001", "Verity", "Pagi")
        self.gerbang = GerbangTol("GT001", "Gerbang Tol Waru")

    def test_tap_masuk(self):
        mobil = Mobil("B6767ABC")
        hasil = self.gerbang.tap_masuk(mobil, self.petugas)
        self.assertEqual(hasil["status"], "berhasil")
        self.assertIn("B6767ABC", self.gerbang.kendaraan_di_dalam)

    def test_tap_masuk_tanpa_petugas(self):
        mobil = Mobil("B6767ABC")
        with self.assertRaises(TypeError):
            self.gerbang.tap_masuk(mobil, None)

    def test_kendaraan_tidak_layak(self):
        class PetugasPalsu:
            id_petugas = "PTG999"
            def validasi_kelayakan(self, kendaraan):
                return False

        mobil = Mobil("B6767ABC")
        with self.assertRaises(ValueError):
            self.gerbang.tap_masuk(mobil, PetugasPalsu())

    def test_tap_masuk_dua_kali(self):
        mobil = Mobil("B6767ABC")
        self.gerbang.tap_masuk(mobil, self.petugas)
        with self.assertRaises(ValueError):
            self.gerbang.tap_masuk(mobil, self.petugas)

    def test_tap_keluar_mobil(self):
        mobil = Mobil("B6767ABC")
        self.gerbang.tap_masuk(mobil, self.petugas)
        transaksi = self.gerbang.tap_keluar("B6767ABC", 10, self.petugas)
        self.assertEqual(transaksi["nomor_plat"], "B6767ABC")
        self.assertEqual(transaksi["golongan"], 1)
        self.assertEqual(transaksi["jarak"], 10)
        self.assertEqual(transaksi["tarif"], 15000)
        self.assertNotIn("B6767ABC", self.gerbang.kendaraan_di_dalam)

    def test_tap_keluar_bis(self):
        bis = Bis("D3939XYZ")
        self.gerbang.tap_masuk(bis, self.petugas)
        transaksi = self.gerbang.tap_keluar("D3939XYZ", 10, self.petugas)
        self.assertEqual(transaksi["golongan"], 2)
        self.assertEqual(transaksi["tarif"], 23000)

    def test_tap_keluar_truk(self):
        truk = Truk("Z9999ZZ", jumlah_sumbu=3)
        self.gerbang.tap_masuk(truk, self.petugas)
        transaksi = self.gerbang.tap_keluar("Z9999ZZ", 10, self.petugas)
        self.assertEqual(transaksi["golongan"], 3)
        self.assertEqual(transaksi["tarif"], 72000)

    def test_tap_keluar_tanpa_tap_masuk(self):
        with self.assertRaises(ValueError):
            self.gerbang.tap_keluar("Z9999ZZ", 10)

    def test_tap_keluar_jarak_tidak_valid(self):
        mobil = Mobil("B6767ABC")
        self.gerbang.tap_masuk(mobil, self.petugas)
        with self.assertRaises(ValueError):
            self.gerbang.tap_keluar("B6767ABC", -10, self.petugas)

    def test_total_pendapatan(self):
        mobil = Mobil("B6767ABC")
        bis = Bis("D3939XYZ")
        truk = Truk("Z9999ZZ", jumlah_sumbu=3)
        self.gerbang.tap_masuk(mobil, self.petugas)
        self.gerbang.tap_masuk(bis, self.petugas)
        self.gerbang.tap_masuk(truk, self.petugas)
        self.assertEqual(self.gerbang.total_pendapatan(), 0)
        self.gerbang.tap_keluar("B6767ABC", 10, self.petugas)
        self.gerbang.tap_keluar("D3939XYZ", 10, self.petugas)
        self.gerbang.tap_keluar("Z9999ZZ", 10, self.petugas)
        self.assertEqual(self.gerbang.total_pendapatan(), 110000)

    def test_tampilkan_riwayat(self):
        mobil = Mobil("B6767ABC")
        self.gerbang.tap_masuk(mobil, self.petugas)
        self.gerbang.tap_keluar("B6767ABC", 10, self.petugas)
        riwayat = self.gerbang.tampilkan_riwayat()
        self.assertEqual(len(riwayat), 1)
        self.assertEqual(riwayat[0]["nomor_plat"], "B6767ABC")

if __name__ == "__main__":
    unittest.main()
