import tkinter as tk
import config as colores

class Registro(tk.Frame):
    def __init__(self, parent, mostrar_principal, mostrar_login):
        super().__init__(parent)
        self.configure(background=colores.FONDO_PRINCIPAL)

        self.label = tk.Label(self, text='Registro', font=('Roboto', 30)).pack()

        self.boton = tk.Button(self, width=20, height=5, bg='blue', text='login in', command=mostrar_principal).pack(side='top')
        self.boton_login = tk.Button(self, width=20, height=5, bg='red', text='volver', command=mostrar_login).pack(side='top')

        self.place(x=0,y=0, relheight=1, relwidth=1)
       

