import tkinter as tk
import config as colores

class Principal(tk.Frame):
    def __init__(self, parent, mostrar_login, mostrar_PuntoVenta):
        super().__init__(parent)
        self.configure(background=colores.BOTON_PRODUCTOS)
        self.place(x=0,y=0, relheight=1, relwidth=1)
 
        self.label = tk.Label(self, text='Principal', font=('Roboto', 30)).pack()
        self.botonP = tk.Button(self, text='Punto de venta', width=20, height=5, bg='green', command=mostrar_PuntoVenta).pack(side='top')
        self.boton = tk.Button(self, width=20, height=5, bg='blue', text='salir', command=mostrar_login).pack(side='top')
        
