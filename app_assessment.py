import random
from pathlib import Path


def baca_bank_soal():
    lokasi_file = Path(__file__).with_name("bank_soal.txt")
    daftar_soal = []

    try:
        with open(lokasi_file, "r", encoding="utf-8-sig") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue

                if "|" not in baris:
                    print(f"Format soal pada baris {nomor_baris} tidak valid.")
                    continue

                pertanyaan, daftar_jawaban = baris.split("|", 1)
                pertanyaan = pertanyaan.strip()
                jawaban = [pilihan.strip() for pilihan in daftar_jawaban.split(",")]

                if not pertanyaan or len(jawaban) != 4 or any(not pilihan for pilihan in jawaban):
                    print(f"Format soal pada baris {nomor_baris} tidak valid.")
                    continue

                if len(set(jawaban)) != 4:
                    print(f"Pilihan jawaban pada baris {nomor_baris} harus berbeda.")
                    continue

                daftar_soal.append((pertanyaan, jawaban))
    except FileNotFoundError:
        print(f"File bank soal tidak ditemukan: {lokasi_file}")
    except OSError as error:
        print(f"Bank soal tidak dapat dibaca: {error}")

    return daftar_soal


def jalankan_assessment():
    semua_soal = baca_bank_soal()

    if len(semua_soal) < 10:
        print("Bank soal harus berisi minimal 10 soal.")
        return

    soal_terpilih = random.sample(semua_soal, 10)
    skor = 0
    pilihan_huruf = ["A", "B", "C", "D"]

    print("=== ASSESSMENT ARITMATIKA ===")
    print("Jawab 10 soal berikut dengan memilih A, B, C, atau D.\n")

    for nomor, (pertanyaan, jawaban) in enumerate(soal_terpilih, start=1):
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)

        print(f"{nomor}. {pertanyaan}")
        for huruf, pilihan in zip(pilihan_huruf, jawaban):
            print(f"   {huruf}. {pilihan}")

        while True:
            jawaban_user = input("Jawaban Anda (A-D): ").strip().upper()
            if jawaban_user in pilihan_huruf:
                break
            print("Masukkan pilihan A, B, C, atau D.")

        indeks_jawaban = pilihan_huruf.index(jawaban_user)
        if jawaban[indeks_jawaban] == jawaban_benar:
            print("Benar!\n")
            skor += 1
        else:
            print(f"Kurang tepat. Jawaban yang benar: {jawaban_benar}\n")

    nilai = skor * 10
    print(f"Assessment selesai. Skor Anda: {skor} dari 10.")
    print(f"Nilai akhir: {nilai}")


jalankan_assessment()
