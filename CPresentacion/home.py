import tkinter as tk
import config as color

from PIL import Image, ImageTk  # Asegúrate de tener instalada la librería Pillow

class Home(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.fondo_imagen = Image.open("imagenes/fondo.jpg")  # Cambia la ruta si es necesario
        self.fondo_imagen = self.fondo_imagen.resize((parent.winfo_width(), parent.winfo_height()), Image.Resampling.LANCZOS)  # Usa LANCZOS en lugar de ANTIALIAS
        self.fondo_imagen_tk = ImageTk.PhotoImage(self.fondo_imagen)

        self.fondo_label = tk.Label(self, image=self.fondo_imagen_tk)
        self.fondo_label.place(relwidth=1, relheight=1)

        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)