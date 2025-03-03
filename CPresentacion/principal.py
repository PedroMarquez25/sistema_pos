import tkinter as tk
import config as colores

class Principal(tk.Frame):
    def __init__(self, parent, mostrar_login, mostrar_PuntoVenta):
        super().__init__(parent)
        self.configure(background=colores.FONDO_PRINCIPAL)
        self.place(x=0,y=0, relheight=1, relwidth=1)

        self.paneles()
        self.crear_widgets()


    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=colores.COLOR_SEGUNDARIO, height=70)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.panel_izquierdo = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=270)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.cuerpo = tk.Frame(self, background=colores.FONDO_SEGUNDARIO, bd=2)
        self.cuerpo.pack(side=tk.RIGHT, fill='both' ,expand=True, padx=10, pady=10)
        
    def crear_widgets(self):
        pass
