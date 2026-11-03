from datetime import datetime
from typing import List
from .kendaraan import Kendaraan

class GerbangTol:
    def __init__(self, id_gerbang: str, nama_gerbang: str):
        self.id_gerbang = id_gerbang
        self.nama_gerbang = nama_gerbang
        self.kendaraan_di_dalam = {}
        self.riwayat_transaksi: List[dict] = []

    def tap_masuk(self, k: Kendaraan, petugas):
        if not isinstance(k, Kendaraan):
            raise TypeError("Objek harus merupakan Kendaraan.")

        if petugas is None or not callable(getattr(petugas, "validasi_kelayakan", None)):
            raise TypeError("Petugas tidak valid.")

        if not petugas.validasi_kelayakan(k):
            raise ValueError("Kendaraan tidak lolos validasi kelayakan.")

        plat = k.nomor_plat.strip()
        if plat in self.kendaraan_di_dalam:
            raise ValueError(f"Kendaraan {plat} sudah melakukan tap masuk.")

        data_masuk = {"kendaraan": k,
                      "waktu_masuk": datetime.now().astimezone().isoformat(timespec="seconds"),
                      "id_petugas_masuk": petugas.id_petugas}
        self.kendaraan_di_dalam[plat] = data_masuk

        return {"status": "berhasil",
                "pesan": f"Kendaraan {plat} berhasil tap masuk",
                "nomor_plat": plat,
                "golongan": k.golongan,
                "waktu_masuk": data_masuk["waktu_masuk"]}

    def tap_keluar(self, nomor_plat: str, jarak: float, petugas=None):
        if not isinstance(nomor_plat, str) or not nomor_plat.strip():
            raise ValueError("Nomor plat harus diisi")
        if (not isinstance(jarak, (int, float)) or isinstance(jarak, bool) or jarak <= 0):
            raise ValueError("Jarak harus berupa angka positif")

        plat = nomor_plat.strip()
        if plat not in self.kendaraan_di_dalam:
            raise ValueError(f"Kendaraan {plat} belum melakukan tap masuk atau sudah melakukan tap keluar")
        if petugas is not None and not hasattr(petugas, "id_petugas"):
            raise TypeError("Petugas keluar tidak valid")

        data_masuk = self.kendaraan_di_dalam[plat]
        kendaraan = data_masuk["kendaraan"]
        tarif = kendaraan.hitung_tarif(jarak)
        waktu_keluar = datetime.now().astimezone().isoformat(timespec="seconds")
        transaksi = {"id_gerbang": self.id_gerbang,
                     "nama_gerbang": self.nama_gerbang,
                     "nomor_plat": plat,
                     "golongan": kendaraan.golongan,
                     "jarak": jarak,
                     "waktu_masuk": data_masuk["waktu_masuk"],
                     "waktu_keluar": waktu_keluar,
                     "tarif": tarif,
                     "id_petugas_masuk": data_masuk["id_petugas_masuk"],
                     "id_petugas_keluar": (getattr(petugas, "id_petugas", None))}
        self.riwayat_transaksi.append(transaksi)
        del self.kendaraan_di_dalam[plat]

        return transaksi.copy()

    def total_pendapatan(self) :
        return sum(transaksi["tarif"] for transaksi in self.riwayat_transaksi)

    def tampilkan_riwayat(self):
        return [transaksi.copy() for transaksi in self.riwayat_transaksi]
