import tkinter as tk
import config as colores
import time

from tkinter import ttk, messagebox
from tkinter import font
from BDominio.usuarios.validar_usuario import UsuarioValid

class Login(tk.Frame):
    def __init__(self, parent, mostrar_registro, mostrar_principal, mostrar_PuntoVenta):
        super().__init__(parent)
        self.config(background=colores.COLOR_SEGUNDARIO)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_principal = mostrar_principal
        self.mostrar_registro = mostrar_registro
        self.mostrar_PuntoVenta = mostrar_PuntoVenta

        self.crear_formulario()
        self.crear_widgets()
     
    def crear_formulario(self):
        self.formulario = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=420, height=500)
        self.formulario.pack(pady=100, anchor='center')
        self.formulario.pack_propagate(False)

    def crear_widgets(self):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=45)

        titulo = tk.Label(self.formulario, text='Quicksale', fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, font=('Montserrat',30, 'bold'))
        titulo.pack(side='top', pady=10)

        icono = tk.Label(self.formulario, text='\uf0c0', font=font_awesome, bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
        icono.pack(side='top', pady=5)

        #=====================================Label y campo usuario===============================================
        etiqueta_usuario = tk.Label(self.formulario, width=30 ,text='Usuario', font=('roboto', 14) ,fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, anchor=tk.W)
        etiqueta_usuario.pack(side='top', pady=5)

        self.entry_usuario = ttk.Entry(self.formulario, width=30, font=('Roboto', 14))
        self.entry_usuario.pack(ipady=5, side='top', pady=5)

        #====================================Label y campo clave===================================================
        etiqueta_clave = tk.Label(self.formulario, width=30 ,text='Contraseña', font=('roboto', 14) ,fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, anchor=tk.W)
        etiqueta_clave.pack(side='top', pady=5)

        self.entry_clave = ttk.Entry(self.formulario, width=30, font=('Roboto', 14))
        self.entry_clave.pack(side='top',ipady=5, pady=5)
        self.entry_clave.config(show="*")


        #======================================Botones de inicio y registro============================================

        self.boton_login = tk.Button(self.formulario, width=13, text='Login in', font=('Roboto', 14,'bold'), bd=0
                                     ,bg=colores.BOTON_PRODUCTOS,command=self.login_in)
        self.boton_login.pack(pady=15, ipady=4)

        self.boton_registro = tk.Button(self.formulario, width=10, text='Registrarse', font=('Roboto',14,'bold'),bd=0,
                                        background=colores.BOTON_PRODUCTOS ,command=self.ir_registro)
        self.boton_registro.pack(ipady=4)
    
    def login_in(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()
        validar = UsuarioValid()

        if len(usuario) == 0 or len(clave) == 0:
            messagebox.showerror(title='Mensaje', message='Complete los campos')
            return 0

        comprobante = validar.validar(usuario, clave)

        if comprobante == 0:
            messagebox.showerror(message='Contraseña o usuario incorrectos', title='Mensaje')
        elif comprobante == 1:
            self.mostrar_PuntoVenta(usuario)
        elif comprobante == 2:
            self.mostrar_principal(usuario)
            
    def ir_registro(self):
        self.mostrar_registro()
         
        
   



        
       



        


