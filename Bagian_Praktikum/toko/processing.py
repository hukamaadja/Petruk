"""Pemrosesan data: kelas Produk dan Inventaris."""


class Produk:
    def __init__(self, kode, nama, harga, stok, **tambahan):
        self.kode, self.nama, self.harga, self.stok = kode, nama, harga, stok
        self.tambahan = tambahan  # **kwargs: atribut bebas, mis. merek="Aqua"

    def nilai(self):
        return self.harga * self.stok


class Inventaris:
    def __init__(self):
        self.daftar = []

    def tambah(self, produk):
        self.daftar.append(produk)

    def total_nilai(self, *kode):
        """*args: hitung total untuk kode tertentu; tanpa argumen = semua."""
        data = [p for p in self.daftar if not kode or p.kode in kode]
        return sum(p.nilai() for p in data)

    def stok_menipis(self, batas=10):
        return list(filter(lambda p: p.stok <= batas, self.daftar))

    def urutkan_harga(self, menurun=False):
        return sorted(self.daftar, key=lambda p: p.harga, reverse=menurun)

    def cari(self, **kriteria):
        """**kwargs: cari berdasarkan atribut tambahan, mis. cari(merek='Aqua')."""
        return [p for p in self.daftar
                if all(p.tambahan.get(k) == v for k, v in kriteria.items())]

    def laporan(self):
        baris = [f"Jumlah produk: {len(self.daftar)}", f"Total nilai: Rp{self.total_nilai():,}"]
        for p in self.urutkan_harga(menurun=True):  # keyword argument
            baris.append(f"- {p.nama}: Rp{p.harga:,} (stok {p.stok})")
        return baris


if __name__ == "__main__":
    inv = Inventaris()
    inv.tambah(Produk("A1", "Aqua", 4000, 5, merek="Aqua"))
    print(inv.total_nilai(), [p.nama for p in inv.cari(merek="Aqua")])