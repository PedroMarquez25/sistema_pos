import tkinter as tk
import config as colores

class PuntoVenta(tk.Frame):
    def __init__(self, parent, mostrar_login):
        super().__init__(parent)
        self.config(background=colores.FONDO_PRINCIPAL)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.button = tk.Button(self, width=20, height=5, text = 'Salir', command=mostrar_login).pack(side='top')


