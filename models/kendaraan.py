from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, nomor_plat: str, golongan: int):
        self.nomor_plat = nomor_plat
        self.golongan = golongan

    @abstractmethod
    def hitung_tarif(self, jarak: float) -> float:
        
        pass