import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert
import os

# Membuat window root untuk dialog box
root = tk.Tk()
root.withdraw()

# Meminta pengguna untuk memilih file input
input_file = filedialog.askopenfilename(title="Pilih File Input", filetypes=[("Word Document", "*.docx")])

# Menetapkan path folder output (sama dengan path folder input)
output_folder = os.path.dirname(input_file)

# Menetapkan path untuk menyimpan versi PDF dari file (sama dengan path input namun dengan ekstensi PDF)
pdf_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".pdf")

# Mengonversi file menggunakan docx2pdf
convert(input_file, pdf_path)

# Menampilkan pesan berhasil
print(f'{input_file} berhasil dikonversi ke {pdf_path}')