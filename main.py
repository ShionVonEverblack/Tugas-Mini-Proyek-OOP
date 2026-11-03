import sys
from models import Petugas, GerbangTol, Mobil, Bis, Truk

def cetak_garis(karakter="=", panjang=50):
    print(karakter * panjang)

def buat_kendaraan_manual():
    print("\n--- PILIH JENIS KENDARAAN ---")
    print("1. Mobil (Golongan 1)")
    print("2. Bis   (Golongan 2)")
    print("3. Truk  (Golongan 3 - 5)")
    
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()
    plat = input("Masukkan plat nomor (contoh: L 1234 AB): ").strip().upper()
    
    if not plat:
        print("[!] Plat nomor tidak boleh kosong.")
        return None

    if pilihan == "1":
        try:
            kursi = int(input("Jumlah kursi (misal: 5 atau 7): "))
            return Mobil(plat_nomor=plat, jumlah_kursi=kursi)
        except ValueError:
            print("[!] Input jumlah kursi harus berupa angka.")
            return None

    elif pilihan == "2":
        try:
            kapasitas = int(input("Kapasitas penumpang (misal: 40): "))
            return Bis(plat_nomor=plat, kapasitas_penumpang=kapasitas)
        except ValueError:
            print("[!] Input kapasitas penumpang harus angka.")
            return None

    elif pilihan == "3":
        try:
            sumbu = int(input("Jumlah sumbu roda (2/3/4/5): "))
            beban = float(input("Beban muatan (dalam ton): "))
            return Truk(plat_nomor=plat, jumlah_sumbu=sumbu, beban_ton=beban)
        except ValueError:
            print("[!] Input sumbu atau beban tidak valid.")
            return None
    else:
        print("[!] Pilihan jenis kendaraan salah.")
        return None

def main():
    # Setup awal sistem tol
    print("\n" + "=" * 50)
    print("   SISTEM MANAJEMEN GERBANG TOL (FLAT RATE)")
    print("          S1 Kecerdasan Artifisial")
    print("=" * 50)

    # Inisialisasi petugas dan gerbang default
    petugas_aktif = Petugas(id_petugas="P-01", nama="Budi Santoso", shift="Pagi")
    gerbang_aktif = GerbangTol(
        id_gerbang="GT-WARU-01",
        nama_gerbang="Gerbang Tol Waru Utama",
        tarif_golongan={
            1: 9000,
            2: 13500,
            3: 18000,
            4: 22500,
            5: 27000
        }
    )

    while True:
        print(f"\n[Lokasi: {gerbang_aktif.nama_gerbang} | Petugas: {petugas_aktif.nama} ({petugas_aktif.shift})]")
        print("Menu Utama:")
        print("1. Layani Kendaraan Masuk & Bayar Tol")
        print("2. Lihat Riwayat Transaksi Gerbang")
        print("3. Cek Total Pendapatan Tol Hari Ini")
        print("4. Cek Info Petugas & Gerbang")
        print("5. Keluar dari Aplikasi")
        
        opsi = input("\nPilih menu (1-5): ").strip()

        if opsi == "1":
            cetak_garis("-")
            kendaraan = buat_kendaraan_manual()
            if kendaraan is None:
                continue

            print("\n>> Memeriksa kelayakan kendaraan oleh petugas...")
            layak = petugas_aktif.validasi_kelayakan(kendaraan)
            
            if not layak:
                print(f"[X] Kendaraan {kendaraan.plat_nomor} TIDAK LAYAK masuk tol!")
                print("    Alasan: Pelanggaran fisik/muatan/roda tidak memenuhi standar.")
                continue

            print(f"[OK] Kendaraan {kendaraan.plat_nomor} lolos validasi.")
            print(">> Memproses transaksi pembayaran tol flat rate...")
            
            hasil = gerbang_aktif.bayar_tol(kendaraan)
            
            # Cetak struk sederhana
            cetak_garis("*")
            print("             STRUK BUKTI PEMBAYARAN TOL")
            cetak_garis("-")
            print(f" ID Transaksi : {hasil.get('id_transaksi', '-')}")
            print(f" Gerbang      : {gerbang_aktif.nama_gerbang}")
            print(f" Petugas Jaga : {petugas_aktif.nama}")
            print(f" Plat Nomor   : {hasil.get('plat_nomor')}")
            print(f" Golongan     : Golongan {hasil.get('golongan')}")
            print(f" Tarif Flat   : Rp {hasil.get('tarif', 0):,}")
            print(f" Status       : {hasil.get('status', 'Berhasil')}")
            cetak_garis("*")

        elif opsi == "2":
            cetak_garis("-")
            riwayat = gerbang_aktif.tampilkan_riwayat()
            if not riwayat:
                print("Belum ada transaksi kendaraan yang tercatat hari ini.")
            else:
                print(f"DAFTAR RIWAYAT TRANSAKSI ({len(riwayat)} Kendaraan):")
                for idx, t in enumerate(riwayat, start=1):
                    print(f"{idx}. [{t.get('id_transaksi')}] Plat: {t.get('plat_nomor')} | "f"Gol: {t.get('golongan')} | Biaya: Rp {t.get('tarif'):,} | Status: {t.get('status')}")
            cetak_garis("-")

        elif opsi == "3":
            cetak_garis("-")
            total = gerbang_aktif.total_pendapatan()
            jumlah_trx = len(gerbang_aktif.tampilkan_riwayat())
            print(f"Total Pendapatan Gerbang : Rp {total:,}")
            print(f"Total Kendaraan Dilayani : {jumlah_trx} unit")
            cetak_garis("-")

        elif opsi == "4":
            cetak_garis("-")
            print("INFORMASI SISTEM:")
            print(petugas_aktif.tampilkan_info())
            print(f"ID Gerbang     : {gerbang_aktif.id_gerbang}")
            print(f"Nama Gerbang   : {gerbang_aktif.nama_gerbang}")
            print("Daftar Tarif   :")
            for gol, tarif in gerbang_aktif.tarif_golongan.items():
                print(f"  - Golongan {gol} : Rp {tarif:,}")
            cetak_garis("-")

        elif opsi == "5":
            print("\nMenutup sesi gerbang tol. Terima kasih dan selamat bertugas kembali!\n")
            sys.exit(0)

        else:
            print("[!] Pilihan menu tidak tersedia, silakan ketik angka 1 - 5.")

if __name__ == "__main__":
    main()