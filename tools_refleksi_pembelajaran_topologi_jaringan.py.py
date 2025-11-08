import tkinter as tk
from tkinter import messagebox

# ==============================
# Data pertanyaan dan jawaban benar
# ==============================
pertanyaan_dan_jawaban = [
    ("Apa yang dimaksud dengan topologi jaringan?",
     "Topologi jaringan adalah desain atau struktur fisik dan logis yang menggambarkan bagaimana perangkat komputer dihubungkan satu sama lain dalam sebuah jaringan, baik secara fisik maupun logis."),
    ("Sebutkan tiga contoh topologi jaringan!",
     "Bus, Star, Ring"),
    ("Kelebihan topologi star dibandingkan bus adalah?",
     "Jika satu kabel putus, jaringan lain tetap berjalan."),
    ("Mengapa penting memahami jenis topologi jaringan sebelum membuat jaringan?",
     "Karena tiap topologi memiliki kelebihan dan kekurangan yang memengaruhi efisiensi jaringan."),
    ("Topologi jaringan apa yang paling cocok digunakan di sekolah? Jelaskan alasannya.",
     "Topologi star, karena mudah dikelola dan jika satu komputer rusak tidak mengganggu yang lain.")
]

jawaban_pengguna = []
skor = 0


# ==============================
# Fungsi tampilkan pertanyaan
# ==============================
def tampilkan_pertanyaan(index=0):
    global skor
    for widget in root.winfo_children():
        widget.destroy()

    if index < len(pertanyaan_dan_jawaban):
        pertanyaan, jawaban_benar = pertanyaan_dan_jawaban[index]

        tk.Label(
            root,
            text=f"{index + 1}. {pertanyaan}",
            font=("Arial", 22, "bold"),
            wraplength=1200,
            justify="left"
        ).pack(pady=40)

        entry = tk.Text(root, font=("Arial", 18), width=80, height=8)
        entry.pack(pady=20)

        def lanjut():
            global skor
            jawaban = entry.get("1.0", "end-1c").strip()
            jawaban_pengguna.append(jawaban)

            # Cek kebenaran sederhana (berdasarkan kata kunci)
            if jawaban and jawaban.lower() in jawaban_benar.lower():
                skor += 20  # tiap pertanyaan benar = 20 poin

            tampilkan_pertanyaan(index + 1)

        tk.Button(
            root,
            text="Selanjutnya",
            font=("Arial", 20),
            bg="#4CAF50",
            fg="white",
            command=lanjut
        ).pack(pady=20)

    else:
        tampilkan_halaman_nilai()


# ==============================
# Halaman nilai & lanjut ke saran
# ==============================
def tampilkan_halaman_nilai():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Hasil Refleksi Pembelajaran",
        font=("Arial", 28, "bold"),
        fg="#2E86C1"
    ).pack(pady=40)

    tk.Label(
        root,
        text=f"Nilai Anda: {skor} / 100",
        font=("Arial", 24),
        fg="#27AE60"
    ).pack(pady=20)

    tk.Button(
        root,
        text="Lanjut ke Saran Pembelajaran Hari Ini",
        font=("Arial", 20),
        bg="#3498DB",
        fg="white",
        command=tampilkan_halaman_saran
    ).pack(pady=40)


# ==============================
# Halaman saran pembelajaran
# ==============================
def tampilkan_halaman_saran():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Saran Pembelajaran Hari Ini",
        font=("Arial", 28, "bold"),
        fg="#2E86C1"
    ).pack(pady=40)

    tk.Label(
        root,
        text="Tuliskan saran atau perbaikan untuk pembelajaran topologi jaringan hari ini:",
        font=("Arial", 20),
        wraplength=1000
    ).pack(pady=20)

    saran_entry = tk.Text(root, font=("Arial", 18), width=90, height=10)
    saran_entry.pack(pady=20)

    def simpan_dan_selesai():
        saran = saran_entry.get("1.0", "end-1c").strip()

        with open("refleksi_dan_saran_pembelajaran.txt", "w", encoding="utf-8") as file:
            file.write("=== Refleksi Pembelajaran Topologi Jaringan ===\n\n")
            for i, (q, a) in enumerate(pertanyaan_dan_jawaban, 1):
                file.write(f"{i}. {q}\nJawaban Benar: {a}\nJawaban Anda: {jawaban_pengguna[i-1]}\n\n")
            file.write(f"Nilai Akhir: {skor}/100\n\n")
            file.write("=== Saran Pembelajaran Hari Ini ===\n\n")
            file.write(saran)

        messagebox.showinfo("Berhasil", "Refleksi dan saran berhasil disimpan!\nProgram akan ditutup.")
        root.destroy()

    tk.Button(
        root,
        text="Simpan dan Selesai",
        font=("Arial", 20),
        bg="#2E86C1",
        fg="white",
        command=simpan_dan_selesai
    ).pack(pady=30)


# ==============================
# Fungsi keluar dengan tombol ESC
# ==============================
def keluar_dengan_esc(event=None):
    konfirmasi = messagebox.askyesno("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar dari aplikasi?")
    if konfirmasi:
        root.destroy()


# ==============================
# Setup jendela utama (fullscreen)
# ==============================
root = tk.Tk()
root.title("Tools Refleksi Pembelajaran Topologi Jaringan")
root.attributes("-fullscreen", True)

# Binding tombol ESC untuk keluar
root.bind("<Escape>", keluar_dengan_esc)

tampilkan_pertanyaan(0)
root.mainloop()
