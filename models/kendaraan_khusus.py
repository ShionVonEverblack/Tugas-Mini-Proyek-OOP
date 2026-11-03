from .kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self, nomor_plat: str):
        super().__init__(nomor_plat, golongan=1)

    def hitung_tarif(self, jarak: float) -> float:
        return 5000 + (jarak * 1000)


class Bis(Kendaraan):
    def __init__(self, nomor_plat: str):
        super().__init__(nomor_plat, golongan=2)

    def hitung_tarif(self, jarak: float) -> float:
        return 8000 + (jarak * 1500)


class Truk(Kendaraan):
    def __init__(self, nomor_plat: str, jumlah_sumbu: int = 2):
        super().__init__(nomor_plat, golongan=3)
        self.jumlah_sumbu = jumlah_sumbu

    def hitung_tarif(self, jarak: float) -> float:
        return 12000 + (jarak * 2000 * self.jumlah_sumbu)