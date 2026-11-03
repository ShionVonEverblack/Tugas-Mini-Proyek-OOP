from models import Petugas, GerbangTol, Mobil, Bis, Truk


def rupiah(nominal):
    return "Rp " + f"{nominal:,.0f}".replace(",", ".")


def main():
    print("=" * 50)
    print("DEMO SIMULASI SISTEM MANAJEMEN TOL".center(50))
    print("=" * 50)

    petugas = Petugas("PTG001", "Verity", "Pagi")
    gerbang = GerbangTol("GT01", "Gerbang Tol Waru")
    print(petugas.tampilkan_info())
    print("Gerbang:", gerbang.nama_gerbang)

    antrean = [
        (Mobil("L1234AB"), 10),
        (Bis("W7001AA"), 25),
        (Truk("N8821UQ", jumlah_sumbu=3), 15),
        (Mobil("B3344CD"), 7.5),
    ]

    print("\n[1] Tap masuk")
    for kendaraan, _ in antrean:
        hasil = gerbang.tap_masuk(kendaraan, petugas)
        print(f"  {type(kendaraan).__name__:<6} -> {hasil['pesan']}")

    try:
        gerbang.tap_masuk(antrean[0][0], petugas)
    except ValueError as e:
        print("  Ditolak:", e)

    print("\n[2] Tap keluar")
    for kendaraan, jarak in antrean:
        struk = gerbang.tap_keluar(kendaraan.nomor_plat, jarak, petugas)
        print(f"  {struk['nomor_plat']:<9} gol {struk['golongan']} | "
              f"{jarak:>4} km | {rupiah(struk['tarif'])}")

    try:
        gerbang.tap_keluar("AB9999XX", 5, petugas)
    except ValueError as e:
        print("  Ditolak:", e)

    print("\n[3] Rekap")
    print("  Jumlah transaksi :", len(gerbang.tampilkan_riwayat()))
    print("  Total pendapatan :", rupiah(gerbang.total_pendapatan()))
    print("=" * 50)


if __name__ == "__main__":
    main()