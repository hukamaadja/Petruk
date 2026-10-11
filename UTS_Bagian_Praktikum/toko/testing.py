"""Unit test memakai unittest."""
import unittest
from toko.validasi import validasi_baris, DataError
from toko.processing import Produk, Inventaris


class TestToko(unittest.TestCase):
    def setUp(self):
        self.inv = Inventaris()
        self.inv.tambah(Produk("A1", "Aqua", 4000, 5, merek="Aqua"))
        self.inv.tambah(Produk("A2", "Beras", 68000, 40))

    def test_validasi_benar(self):
        self.assertEqual(validasi_baris("A1,Aqua,4000,5"), ("A1", "Aqua", 4000, 5))

    def test_nilai_negatif(self):
        with self.assertRaises(DataError):
            validasi_baris("A1,Aqua,-1,5")

    def test_total_nilai_args(self):
        self.assertEqual(self.inv.total_nilai("A1"), 20000)
        self.assertEqual(self.inv.total_nilai(), 20000 + 2720000)

    def test_stok_menipis(self):
        self.assertEqual([p.kode for p in self.inv.stok_menipis(batas=5)], ["A1"])

    def test_cari_kwargs(self):
        self.assertEqual(len(self.inv.cari(merek="Aqua")), 1)


if __name__ == "__main__":
    unittest.main()