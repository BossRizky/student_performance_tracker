"""Modul Penilaian: menyimpan nilai tugas dan menghitung nilai akhir."""

class Penilaian:
    def __init__(self, quiz, tugas, uts, uas):
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def nilai_akhir(self):
        for n in [self.quiz, self.tugas, self.uts, self.uas]:
            if not 0 <= n <= 100:
                raise ValueError("Nilai harus 0–100")
        return round((self.quiz * 0.15) + (self.tugas * 0.25) + (self.uts * 0.25) + (self.uas * 0.35), 2)
