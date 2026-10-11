"""Baca/tulis file, selalu dengan `with open()`."""
from toko.validasi import validasi_baris
from toko.processing import Produk, Inventaris


def buat_file(path):
    """Mode 'x': buat file baru; gagal jika sudah ada agar data lama tidak tertimpa."""
    try:
        with open(path, "x") as f:
            f.write("")
        return True
    except FileExistsError:
        print(f"File '{path}' sudah ada, tidak dibuat ulang.")
        return False


def tambah_baris(path, teks):
    """Mode 'a': tambah data di akhir tanpa menghapus isi lama."""
    with open(path, "a") as f:
        f.write(teks + "\n")


def baca_data(path):
    """Mode 'r': baca baris demi baris; baris rusak dilewati."""
    inv = Inventaris()
    try:
        with open(path, "r") as f:
            for baris in f:
                try:
                    kode, nama, harga, stok = validasi_baris(baris)
                    inv.tambah(Produk(kode, nama, harga, stok))
                except ValueError as err:  # termasuk DataError
                    print("Dilewati:", err)
    except FileNotFoundError:
        print(f"File '{path}' tidak ditemukan. Buat dulu dengan buat_file().")
    return inv


def tulis_laporan(path, baris):
    """Mode 'w': laporan dibuat ulang setiap kali, jadi boleh menimpa."""
    with open(path, "w") as f:
        f.write("\n".join(baris) + "\n")


if __name__ == "__main__":
    baca_data("tidak_ada.txt")