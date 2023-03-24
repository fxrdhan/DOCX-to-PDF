import tkinter as tk
from tkinter import filedialog
import os
from docx2pdf import convert

# Membuat window root untuk dialog box
root = tk.Tk()
root.withdraw()

# Meminta pengguna untuk memilih folder input
folder_input = filedialog.askdirectory(title="Pilih Folder Input")

folder_output = folder_input

# Loop melalui file di dalam folder input
for file in os.listdir(folder_input):
    # Cek apakah file adalah file .docx
    if file.endswith('.docx'):
        # Konversi file .docx menjadi PDF dan simpan ke dalam folder output
        docx_path = os.path.join(folder_input, file)
        pdf_path = os.path.join(folder_output, file.replace(".docx", ".pdf"))
        convert(docx_path, pdf_path)
        
        # Menampilkan pesan berhasil
        print(f'{file} berhasil dikonversi')
