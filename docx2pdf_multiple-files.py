import tkinter as tk
from tkinter import filedialog
import os
from docx2pdf import convert

# Buat window untuk dialog box
window = tk.Tk()
window.withdraw()

# Pilih folder input
folder_input = filedialog.askdirectory(title="Pilih Folder Input")
# Buat file output terletak pada direktori asalnya
folder_output = folder_input

# Loop file di dalam folder input
for file in os.listdir(folder_input):
    # Cek apakah file adalah file .docx
    if file.endswith('.docx'):
        # Konversi file .docx menjadi PDF dan simpan ke dalam folder output
        docx_path = os.path.join(folder_input, file)
        pdf_path = os.path.join(folder_output, file.replace(".docx", ".pdf"))
        convert(docx_path, pdf_path)
        
        # Tampilkan pesan berhasil
        print(f'{file} berhasil dikonversi')
