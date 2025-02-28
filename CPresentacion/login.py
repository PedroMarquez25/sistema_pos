import tkinter as tk
import config as colores

from tkinter import font
from BDominio.usuarios.validar_usuario import validar


class Login(tk.Frame):
    def __init__(self, parent, mostrar_registro, mostrar_principal):
        super().__init__(parent)
        self.config(background=colores.COLOR_SEGUNDARIO)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_principal = mostrar_principal
        self.mostrar_registro = mostrar_registro

        self.crear_formulario()
        self.crear_widgets()
     

    def crear_formulario(self):
        self.formulario = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=450, height=500)
        self.formulario.pack(pady=100, anchor='center')
        self.formulario.pack_propagate(False)

    def crear_widgets(self):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=45)

        titulo = tk.Label(self.formulario, text='Quicksale', fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, font=('Montserrat',30, 'bold'))
        titulo.pack(side='top', pady=5)

        icono = tk.Label(self.formulario, text='\uf0c0', font=font_awesome, bg=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        icono.pack(side='top', pady=3)

        #label
        etiqueta_usuario = tk.Label(self.formulario, width=30 ,text='Usuario', font=('roboto', 14) ,fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, anchor=tk.W)
        etiqueta_usuario.pack(side='top', pady=3)


        self.entry_usuario = tk.Entry(self.formulario, width=30, font=('Roboto', 14))
        self.entry_usuario.pack(ipady=4, side='top')


        etiqueta_clave = tk.Label(self.formulario, width=30 ,text='Contraseña', font=('roboto', 14) ,fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL, anchor=tk.W)
        etiqueta_clave.pack(side='top', pady=10)


        self.entry_clave = tk.Entry(self.formulario, width=30, font=('Roboto', 14))
        self.entry_clave.pack(side='top',ipady=4)


        self.label_mensaje = tk.Label(self.formulario, background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, text='mensaje', font=('roboto', 10))
        self.label_mensaje.pack(pady=10)

        #Botones

        self.boton_login = tk.Button(self.formulario, width=13, text='Login in', font=('Roboto', 14)
                                     ,bg=colores.BOTON_PRODUCTOS, command=self.login_in)
        self.boton_login.pack(pady=10)

        self.boton_registro = tk.Button(self.formulario, width=10, text='Regitrarse', font=('Roboto',14),
                                        background=colores.BOTON_PRODUCTOS, command=self.ir_registro)
        self.boton_registro.pack(pady=2)
    
    def login_in(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()

        if validar(usuario, clave):
            self.mostrar_principal()
            self.entry_clave.delete(0,'end')
            self.entry_usuario.delete(0,'end')
            self.label_mensaje.config(text='')
        else:
            self.label_mensaje.config(text='Contraseña o usuario incorrectos', fg='red')

        

    def ir_registro(self):
        self.mostrar_registro()
         
        
   



        
       



        


