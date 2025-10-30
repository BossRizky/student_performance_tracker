import csv
import os

DATA_FILE = "data/student_data.csv"

class RekapKelas:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        # Buat file CSV kalau belum ada
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["nim", "nama", "hadir", "quiz", "tugas", "uts", "uas", "nilai_akhir"])
        self.data = self._load_data()

    # Membaca semua data dari CSV
    def _load_data(self):
        data = []
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    # Menyimpan semua data ke CSV
    def _save_data(self):
        with open(DATA_FILE, "w", newline="") as f:
            fieldnames = ["nim", "nama", "hadir", "quiz", "tugas", "uts", "uas", "nilai_akhir"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    # Tambah mahasiswa baru
    def tambah_mahasiswa(self, nim, nama, hadir):
        self.data.append({
            "nim": nim,
            "nama": nama,
            "hadir": hadir,
            "quiz": 0,
            "tugas": 0,
            "uts": 0,
            "uas": 0,
            "nilai_akhir": 0
        })
        self._save_data()

    # Ubah nilai mahasiswa
    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        for mhs in self.data:
            if mhs["nim"] == nim:
                mhs["quiz"] = quiz
                mhs["tugas"] = tugas
                mhs["uts"] = uts
                mhs["uas"] = uas
                # Hitung nilai akhir (bobot: Quiz 10%, Tugas 20%, UTS 30%, UAS 40%)
                nilai_akhir = 0.1*quiz + 0.2*tugas + 0.3*uts + 0.4*uas
                mhs["nilai_akhir"] = round(nilai_akhir, 2)
        self._save_data()

    # Hapus mahasiswa berdasarkan NIM
    def hapus_mahasiswa(self, nim):
        self.data = [m for m in self.data if m["nim"] != nim]
        self._save_data()

    # Menampilkan semua data (atau filter)
    def rekap(self, filter_nilai=None):
        result = []
        for mhs in self.data:
            if filter_nilai:
                if float(mhs["nilai_akhir"]) < filter_nilai:
                    result.append(mhs)
            else:
                result.append(mhs)
        return result
