"""Validasi data. Format baris: kode,nama,harga,stok"""


class DataError(ValueError):
    """Eksepsi kustom untuk data janggal (negatif / kosong)."""


def validasi_baris(baris):
    assert isinstance(baris, str), "baris harus berupa string"  # cek kesalahan programmer
    kolom = [k.strip() for k in baris.split(",")]
    if len(kolom) != 4 or "" in kolom:
        raise DataError(f"Kolom kosong atau jumlah kolom salah: {baris.strip()}")
    kode, nama, harga, stok = kolom
    harga, stok = int(harga), int(stok)  # bisa memunculkan ValueError
    if harga < 0 or stok < 0:
        raise DataError(f"Harga/stok tidak boleh negatif: {baris.strip()}")
    return kode, nama, harga, stok


if __name__ == "__main__":
    print(validasi_baris("B1,Beras,68000,40"))