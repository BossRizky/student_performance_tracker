"""Aplikasi utama Student Performance Tracker (CLI)."""

from tracker.rekap_kelas import RekapKelas
from tracker.report import Report

def main():
    rekap = RekapKelas()
    report = Report()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Tambah mahasiswa")
        print("2) Ubah penilaian")
        print("3) Hapus mahasiswa")
        print("4) Lihat rekap")
        print("5) Simpan laporan Markdown")
        print("6) Simpan laporan HTML")
        print("7) Lihat mahasiswa nilai < 70")
        print("8) Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            nim = input("NIM: ")
            nama = input("Nama: ")
            hadir = float(input("Hadir (%): "))
            rekap.tambah_mahasiswa(nim, nama, hadir)
            print("Mahasiswa ditambahkan.")

        elif pilih == "2":
            nim = input("NIM: ")
            q, t, uts, uas = [float(input(f"{n}: ")) for n in ["Quiz", "Tugas", "UTS", "UAS"]]
            rekap.set_penilaian(nim, q, t, uts, uas)
            print("Nilai diperbarui.")

        elif pilih == "3":
            nim = input("Masukkan NIM yang ingin dihapus: ")
            rekap.hapus_mahasiswa(nim)
            print("Data mahasiswa dihapus.")

        elif pilih == "4":
            print("\n=== REKAP MAHASISWA ===")
            for r in rekap.rekap():
                print(r)

        elif pilih == "5":
            konten = report.build_markdown_report(rekap.rekap())
            report.save_text("out/report.md", konten)
            print("Laporan Markdown tersimpan di out/report.md")

        elif pilih == "6":
            report.save_html("out/report.html", rekap.rekap())
            print("Laporan HTML tersimpan di out/report.html")

        elif pilih == "7":
            print("\nMahasiswa dengan nilai akhir < 70:")
            for r in rekap.rekap(filter_nilai=70):
                print(r)

        elif pilih == "8":
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
