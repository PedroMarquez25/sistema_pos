import tkinter as tk
import config as colores

class PuntoVenta(tk.Frame):
    def __init__(self, parent, mostrar_login):
        super().__init__(parent)
        self.config(background=colores.FONDO_PRINCIPAL)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.paneles()

        
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=colores.COLOR_SEGUNDARIO, height=70)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.panel_izquierdo = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=196)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.list_productos = tk.Frame(self, bg=colores.BOTON_PRODUCTOS, width=667)
        self.list_productos.pack(side=tk.LEFT, fill=tk.Y ,padx=5, pady=5)

        self.factura = tk.Frame(self, bg=colores.BOTON_VENTAS, width=480)
        self.factura.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)





