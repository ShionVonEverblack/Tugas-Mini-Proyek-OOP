from models import Petugas, GerbangTol, Mobil, Bis, Truk

def jalankan_demo():
    print("=" * 60)
    print("     DEMONSTRASI SISTEM MANAJEMEN TOL (FLAT RATE)")
    print("=" * 60)

    # 1. Inisialisasi Objek Petugas & Gerbang
    petugas = Petugas(id_petugas="PTG-007", nama="Siti Aminah", shift="Siang")
    gerbang = GerbangTol(
        id_gerbang="GT-DUPAK-02",
        nama_gerbang="Gerbang Tol Dupak Surabaya",
        tarif_golongan={
            1: 8500,
            2: 12500,
            3: 17000,
            4: 21500,
            5: 26000
        }
    )

    print(f">> Petugas Berjaga : {petugas.nama} ({petugas.shift})")
    print(f">> Gerbang Operasi : {gerbang.nama_gerbang}")
    print("-" * 60)

    # 2. Siapkan Sampel Berbagai Jenis Kendaraan (Polimorfisme)
    daftar_kendaraan = [
        Mobil(plat_nomor="L 1945 RI", jumlah_kursi=7),
        Bis(plat_nomor="W 7001 AA", kapasitas_penumpang=45),
        Truk(plat_nomor="N 8821 UQ", jumlah_sumbu=3, beban_ton=14.0),
        Mobil(plat_nomor="B 3344 CD", jumlah_kursi=4),
        Truk(plat_nomor="DK 9901 AB", jumlah_sumbu=5, beban_ton=35.0), # Truk besar
    ]

    print(f"Total kendaraan yang mengantre: {len(daftar_kendaraan)} unit.\n")

    # 3. Alur Pemrosesan Antrean
    for no, k in enumerate(daftar_kendaraan, start=1):
        print(f"--- [Antrean {no}] ---")
        print(f"Info Kendaraan : {k.tampilkan_info()}")
        
        # Validasi fisik oleh petugas
        apakah_layak = petugas.validasi_kelayakan(k)
        if not apakah_layak:
            print(f"Status Cek     : DITOLAK oleh {petugas.nama} (Tidak memenuhi syarat fisik)")
            continue
        
        print("Status Cek     : DITERIMA (Lolos verifikasi kelayakan)")
        
        # Hitung tarif dan bayar tol flat rate
        tarif = gerbang.hitung_tarif(k)
        transaksi = gerbang.bayar_tol(k)
        
        print(f"Biaya Masuk    : Rp {tarif:,}")
        print(f"ID Struk       : {transaksi.get('id_transaksi')}")
        print(f"Status Bayar   : {transaksi.get('status')}\n")

    # 4. Ringkasan Akhir
    print("=" * 60)
    print("               LAPORAN AKHIR SHIFT GERBANG")
    print("=" * 60)
    print(f"Nama Gerbang           : {gerbang.nama_gerbang}")
    print(f"Total Kendaraan Sukses : {len(gerbang.tampilkan_riwayat())} unit")
    print(f"Total Uang Masuk       : Rp {gerbang.total_pendapatan():,}")
    print("=" * 60)
    print("[*] Simulasi selesai dijalankan dengan sukses.")

if __name__ == "__main__":
    jalankan_demo()