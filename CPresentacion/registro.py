import tkinter as tk
import config as colores

from tkinter import ttk, messagebox, font

class Registro(tk.Frame):
    def __init__(self, parent, mostrar_principal, mostrar_login):
        super().__init__(parent)
        self.configure(background=colores.COLOR_SEGUNDARIO)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_principal = mostrar_principal
        self.mostrar_login = mostrar_login

        self.crear_formulario()
        self.crear_widgets()


        
    def crear_formulario(self):
        self.formulario = tk.Frame(self, width=400, height=400, bg=colores.COLOR_PRINCIPAL, bd=0)
        self.formulario.pack(pady=160)
        self.formulario.pack_propagate(False)
    
    def crear_widgets(self):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=35)

        self.frame_titulo = tk.Frame(self.formulario, bg=colores.COLOR_PRINCIPAL, height=100)
        self.frame_titulo.pack(side='top',fill='x')

        self.frame_codigo = tk.Frame(self.formulario, bg=colores.COLOR_PRINCIPAL, height=200)
        self.frame_codigo.pack(side='top',fill='x')

        #frame titulo
        label_titulo = tk.Label(self.frame_titulo, text='Registrarse', font=('Montserrat',20, 'bold'), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        label_titulo.pack(pady=10)
 
        icono = tk.Label(self.frame_titulo, text='\uf509', font=font_awesome, bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
        icono.pack(pady=5)
        


        #frame codigo
        label_codigo = tk.Label(self.frame_codigo, text='Codigo de registro' ,font=('roboto', 14),
                                    fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL ,anchor='w')
        label_codigo.pack(fill='x', padx=30, pady=2, ipady=5)


        self.entry_codigo = ttk.Entry(self.frame_codigo, font=('time', 18), show="*")
        self.entry_codigo.pack(fill='x', padx=30,pady=5 ,ipady=5)

        self.boton_registrar = tk.Button(self.frame_codigo, text='Registrar', width=15,height=1, font=('Roboto', 14, 'bold'),
                                          bd=0, bg=colores.BOTON_PRODUCTOS)
        self.boton_registrar.pack(pady=10, ipady=2)

        self.boton_regresar = tk.Button(self.frame_codigo, text='Regresar', width=12,height=1, font=('Roboto', 14, 'bold'),
                                          bd=0, bg=colores.BOTON_PRODUCTOS, command=self.ir_login)
        self.boton_regresar.pack(pady=5, ipady=2)

    def ir_login(self):
        self.mostrar_login()
        self.entry_codigo.delete(0, 'end')
        




       

