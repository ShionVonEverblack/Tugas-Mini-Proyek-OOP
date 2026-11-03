from .kendaraan import Kendaraan

class Petugas:
    def __init__(self, id_petugas: str, nama: str, shift: str):
        self.id_petugas = id_petugas
        self.nama = nama
        self.shift = shift

    def validasi_kelayakan(self, k: Kendaraan):
        if not isinstance(k, Kendaraan):
            return False

        plat_valid = (isinstance(k.nomor_plat, str) and bool(k.nomor_plat.strip()))
        golongan_valid = (isinstance(k.golongan, int) and not isinstance(k.golongan, bool) and k.golongan > 0)
        return plat_valid and golongan_valid

    def tampilkan_info(self):
        return (f"ID Petugas: {self.id_petugas} | Nama: {self.nama} | Shift: {self.shift}")
