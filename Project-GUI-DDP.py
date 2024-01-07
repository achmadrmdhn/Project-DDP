import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

def hitung_ukuran():
    try:
        berat_badan = float(entry_berat.get())
        tinggi_badan = float(entry_tinggi.get())
        lingkar_dada = float(entry_lingkar.get())

        # Logic
        if berat_badan < 65 and tinggi_badan < 160 and lingkar_dada < 90:
            hasil = "S"
        elif berat_badan < 75 and tinggi_badan < 165 and lingkar_dada < 100:
            hasil = "M"
        elif berat_badan < 85 and tinggi_badan < 170 and lingkar_dada < 110:
            hasil = "L"
        elif berat_badan < 95 and tinggi_badan < 175 and lingkar_dada < 120:
            hasil = "XL"
        elif berat_badan < 105 and tinggi_badan < 180 and lingkar_dada < 130:
            hasil = "XXL"
        else:
            hasil = "XXXL"

        # Messagebox
        messagebox.showinfo("Hasil", f"Rekomendasi Ukuran Baju Untuk Anda Adalah : Ukuran {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan Angka Yang Valid Untuk Semua Kolom!")

def clear_input():
    entry_berat.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    entry_lingkar.delete(0, tk.END)
    label_hasil.config(text="")

# Membuat jendela utama dengan ukuran, background, resizable, dan title window
root = tk.Tk()
root.title("Program Rekomendasi Ukuran Baju")
root.resizable(False, False)  # Mengatur agar jendela tidak dapat diresize

# Membuat input untuk memasukkan berat badan, tinggi badan, dan lingkar dada
entry_berat = tk.Entry(root, width=20, font=("Helvetica", 12))
entry_tinggi = tk.Entry(root, width=20, font=("Helvetica", 12))
entry_lingkar = tk.Entry(root, width=20, font=("Helvetica", 12))

# Hasil
label_hasil = tk.Label(root, text="", font=("Helvetica", 12))
tombol_hitung = tk.Button(root, text="Hitung Ukuran", command=hitung_ukuran, font=("Helvetica", 12))
tombol_clear = tk.Button(root, text="Clear", command=clear_input, font=("Helvetica", 12))

# Layouting
tk.Label(root, text="Berat Badan (KG):", font=("Helvetica", 12)).grid(row=0, column=0, padx=30, pady=10, sticky='w')
entry_berat.grid(row=0, column=1, padx=10, pady=10, sticky='e')

tk.Label(root, text="Tinggi Badan (CM):", font=("Helvetica", 12)).grid(row=1, column=0, padx=30, pady=10, sticky='w')
entry_tinggi.grid(row=1, column=1, padx=10, pady=10, sticky='e')

tk.Label(root, text="Lingkar Dada (CM):", font=("Helvetica", 12)).grid(row=2, column=0, padx=30, pady=10, sticky='w')
entry_lingkar.grid(row=2, column=1, padx=10, pady=10, sticky='e')

tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)
tombol_clear.grid(row=4, column=0, columnspan=2, pady=10)
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

# Program run
root.mainloop()