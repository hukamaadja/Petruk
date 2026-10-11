"""Program utama inventaris toko."""
import os
import unittest
from toko.fileio import buat_file, tambah_baris, baca_data, tulis_laporan
from toko.testing import TestToko

FILE_DATA, FILE_LAPORAN = "data_toko.txt", "laporan.txt"


def main():
    if buat_file(FILE_DATA):  # isi data awal hanya saat file baru dibuat
        for baris in ["A1,Aqua,4000,6", "A2,Beras,68000,40", "A3,Minyak,38000,8",
                      "A4,Gula,abc,20",       # rusak: harga bukan angka
                      "A5,Teh,-5000,10",      # rusak: negatif
                      "A6,,3000,5"]:          # rusak: kolom kosong
            tambah_baris(FILE_DATA, baris)

    inv = baca_data(FILE_DATA)
    print("Stok menipis:", [p.nama for p in inv.stok_menipis(batas=10)])
    tulis_laporan(FILE_LAPORAN, inv.laporan())
    print("Laporan ditulis ke", FILE_LAPORAN)

    baca_data("tidak_ada.txt")  # demo FileNotFoundError

    unittest.TextTestRunner(verbosity=1).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestToko))


if __name__ == "__main__":
    main()