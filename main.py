from models import Petugas, GerbangTol, Mobil, Bis, Truk


def garis(karakter="-", panjang=45):
    print(karakter * panjang)


def rupiah(nominal):
    return "Rp " + f"{nominal:,.0f}".replace(",", ".")


def rapikan_waktu(waktu_iso):
    return waktu_iso[:19].replace("T", " ")


def input_angka(pesan, tipe=float):
    while True:
        teks = input(pesan).strip()
        try:
            angka = tipe(teks)
        except ValueError:
            print("Harus angka, coba lagi.")
            continue

        if angka <= 0:
            print("Angka harus lebih dari 0.")
            continue
        return angka


def input_petugas():
    print("Data petugas yang berjaga")
    id_petugas = input("ID petugas : ").strip() or "PTG001"
    nama = input("Nama       : ").strip() or "Petugas"

    daftar_shift = {"1": "Pagi", "2": "Siang", "3": "Malam"}
    while True:
        print("Shift: 1. Pagi  2. Siang  3. Malam")
        pilih = input("Pilih shift: ").strip()
        if pilih in daftar_shift:
            return Petugas(id_petugas, nama, daftar_shift[pilih])
        print("Pilihan shift tidak ada.")


def buat_kendaraan():
    print("\nJenis kendaraan:")
    print("1. Mobil (Gol 1)")
    print("2. Bis   (Gol 2)")
    print("3. Truk  (Gol 3)")
    jenis = input("Pilih: ").strip()

    if jenis not in ("1", "2", "3"):
        print("Jenis kendaraan tidak ada.")
        return None

    plat = input("Plat nomor: ").strip().upper()
    if not plat:
        print("Plat nomor tidak boleh kosong.")
        return None

    if jenis == "1":
        return Mobil(plat)
    if jenis == "2":
        return Bis(plat)

    sumbu = input_angka("Jumlah sumbu truk: ", int)
    return Truk(plat, jumlah_sumbu=sumbu)


def menu_tap_masuk(gerbang, petugas):
    kendaraan = buat_kendaraan()
    if kendaraan is None:
        return

    try:
        hasil = gerbang.tap_masuk(kendaraan, petugas)
    except (ValueError, TypeError) as e:
        print("Gagal tap masuk:", e)
        return

    print(hasil["pesan"])
    print("Jenis :", type(kendaraan).__name__, "- Golongan", hasil["golongan"])
    print("Waktu :", rapikan_waktu(hasil["waktu_masuk"]))


def menu_tap_keluar(gerbang, petugas):
    if not gerbang.kendaraan_di_dalam:
        print("Belum ada kendaraan yang tap masuk.")
        return

    print("Kendaraan yang masih di dalam tol:")
    for plat, data in gerbang.kendaraan_di_dalam.items():
        jenis = type(data["kendaraan"]).__name__
        print(f"- {plat} ({jenis})")

    plat = input("Plat nomor yang keluar: ").strip().upper()
    jarak = input_angka("Jarak tempuh (km): ")

    try:
        struk = gerbang.tap_keluar(plat, jarak, petugas)
    except (ValueError, TypeError) as e:
        print("Gagal tap keluar:", e)
        return

    garis("=")
    print("STRUK PEMBAYARAN TOL".center(45))
    garis("=")
    print("Gerbang      :", struk["nama_gerbang"])
    print("Plat nomor   :", struk["nomor_plat"])
    print("Golongan     :", struk["golongan"])
    print("Masuk        :", rapikan_waktu(struk["waktu_masuk"]))
    print("Keluar       :", rapikan_waktu(struk["waktu_keluar"]))
    print("Jarak        :", f"{struk['jarak']:g} km")
    print("Petugas      :", struk["id_petugas_keluar"])
    garis()
    print("TOTAL BAYAR  :", rupiah(struk["tarif"]))
    garis("=")


def menu_pendapatan(gerbang):
    jumlah = len(gerbang.tampilkan_riwayat())
    print("Kendaraan sudah bayar :", jumlah)
    print("Total pendapatan      :", rupiah(gerbang.total_pendapatan()))


def menu_riwayat(gerbang):
    riwayat = gerbang.tampilkan_riwayat()
    if not riwayat:
        print("Belum ada transaksi.")
        return

    print(f"{'No':<4}{'Plat':<12}{'Gol':<5}{'Jarak':<9}{'Tarif':>14}")
    garis()
    for i, t in enumerate(riwayat, start=1):
        jarak = f"{t['jarak']:g} km"
        print(f"{i:<4}{t['nomor_plat']:<12}{t['golongan']:<5}{jarak:<9}{rupiah(t['tarif']):>14}")
    garis()
    print("Total:", rupiah(gerbang.total_pendapatan()))


def main():
    garis("=")
    print("SISTEM MANAJEMEN TOL".center(45))
    garis("=")

    petugas = input_petugas()
    gerbang = GerbangTol("GT01", "Gerbang Tol Waru")

    print()
    print(petugas.tampilkan_info())
    print("Bertugas di", gerbang.nama_gerbang)

    while True:
        print()
        garis()
        print("1. Tap masuk kendaraan")
        print("2. Tap keluar & bayar")
        print("3. Cek total pendapatan")
        print("4. Cetak histori transaksi")
        print("0. Keluar")
        garis()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            menu_tap_masuk(gerbang, petugas)
        elif pilihan == "2":
            menu_tap_keluar(gerbang, petugas)
        elif pilihan == "3":
            menu_pendapatan(gerbang)
        elif pilihan == "4":
            menu_riwayat(gerbang)
        elif pilihan == "0":
            print(f"Shift {petugas.shift} selesai. Terima kasih, {petugas.nama}!")
            break
        else:
            print("Menu tidak ada.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")