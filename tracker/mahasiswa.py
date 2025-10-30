"""Modul Mahasiswa: menyimpan data mahasiswa dan validasi kehadiran."""

class Mahasiswa:
    def __init__(self, nim, nama, hadir_persen):
        self.nim = nim
        self.nama = nama
        self.hadir_persen = hadir_persen

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Persentase hadir harus antara 0–100")
        self._hadir_persen = value

    def info(self):
        return f"{self.nim} - {self.nama} ({self.hadir_persen}%)"
