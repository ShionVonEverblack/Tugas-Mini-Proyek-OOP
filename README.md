# Sistem Manajemen Tol (Flat Rate)

Mini proyek implementasi Pemrograman Berorientasi Objek (OOP) pada Sistem Manajemen Gerbang Tol berbasis tarif tetap (*flat rate*), dikembangkan untuk tugas praktikum S1 Kecerdasan Artifisial Universitas Negeri Surabaya.

## Deskripsi Singkat
Sistem ini memodelkan interaksi antara **Petugas**, **Gerbang Tol**, dan berbagai jenis **Kendaraan** (Mobil, Bis, dan Truk). Petugas bertindak memverifikasi kelaikan fisik kendaraan sebelum memasuki gerbang, sementara gerbang tol bertugas mengklasifikasikan tarif sesuai golongan, memproses transaksi secara *flat rate*, dan mencatat riwayat pembayaran serta total penerimaan uang tol.

## Penerapan Konsep OOP
1. **Inheritance & Abstract Base Class (ABC):**
   - Class `Kendaraan` sebagai *abstract parent class* turunan dari modul `abc`.
   - Subclass `Mobil`, `Bis`, dan `Truk` mewarisi atribut dasar dan meng-override method `tampilkan_info()`.
2. **Polymorphism:**
   - Objek `Mobil`, `Bis`, dan `Truk` dapat diperlakukan seragam sebagai `Kendaraan` pada proses `hitung_tarif(k)` dan `bayar_tol(k)`.
3. **Aggregation:**
   - Class `GerbangTol` memiliki relasi agregasi terhadap objek `Kendaraan` yang dilayaninya.
4. **Association:**
   - Relasi kerja antara `Petugas` yang memvalidasi `Kendaraan`.

---

## Pembagian Kerja Tim (3 Orang)
- **Orang 1 (Hierarki Kendaraan):**
  - `models/kendaraan.py`
  - `models/kendaraan_khusus.py`
  - `tests/test_kendaraan.py`
- **Orang 2 (Gerbang & Petugas):**
  - `models/petugas.py`
  - `models/gerbang_tol.py`
  - `tests/test_petugas.py`
  - `tests/test_gerbang_tol.py`
- **Orang 3 (Integrasi, Interface, & Dokumentasi):**
  - `models/__init__.py`
  - `main.py`
  - `demo_simulasi.py`
  - `requirements.txt`
  - `README.md`

---

## Struktur Direktori
```text
Tugas-Mini-Proyek-OOP/
├── main.py                     # Entry point program (CLI interaktif)
├── demo_simulasi.py            # Skrip demo alur otomatis
├── README.md                   # Panduan dokumentasi proyek
├── requirements.txt            # Keterangan environment sistem
├── models/                     # Package domain OOP
│   ├── __init__.py             # Public module export
│   ├── kendaraan.py            # Abstract Base Class Kendaraan
│   ├── kendaraan_khusus.py     # Class Mobil, Bis, Truk
│   ├── petugas.py              # Class Petugas & validasi
│   └── gerbang_tol.py          # Class GerbangTol & transaksi flat rate
└── tests/                      # Unit testing suite
    ├── test_kendaraan.py
    ├── test_petugas.py
    └── test_gerbang_tol.py