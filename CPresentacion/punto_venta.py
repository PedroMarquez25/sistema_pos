import tkinter as tk
import config as colores

from tkinter import font, messagebox, ttk
from util.util_imagenes import leer_imagen

class PuntoVenta(tk.Frame):
    def __init__(self, parent, mostrar_login, usuario):
        super().__init__(parent)
        self.config(background=colores.FONDO_PRINCIPAL)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_login = mostrar_login
        self.usuario = usuario
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.font_aw = font.Font(family="Font Awesome" ,size=12)

        self.paneles()
        self.widgets_barra_superior()
        self.widgets_panel_izquierdo()
        
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=colores.COLOR_SEGUNDARIO, height=60)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.panel_izquierdo = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=190)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.list_productos = tk.Frame(self, bg=colores.BOTON_PRODUCTOS, width=667)
        self.list_productos.pack(side=tk.RIGHT, fill=tk.BOTH , expand=True, padx=1, pady=5)

        self.factura = tk.Frame(self, bg=colores.BOTON_VENTAS, width=480)
        self.factura.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True ,padx=5, pady=5)
    
    def widgets_barra_superior(self):
         self.icono = tk.Button(self.barra_superior, text= '\uf0c9', font=self.font_awesome,
                               command=self.toggle_panel)
         self.icono.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO, bd=0)
         self.icono.pack(side=tk.LEFT, padx=5)

         self.lbl_nombre = tk.Label(self.barra_superior, text='Quicksale', font=('Montserrat', 20))
         self.lbl_nombre.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
         self.lbl_nombre.pack(side=tk.LEFT)

         #====================crear imagen de perfil con un canvas================

         self.imagen = leer_imagen("c:/Users/pedro/OneDrive/Pictures/fot.jpg", (50,40))

         self.button_perfil = tk.Button(self.barra_superior, image=self.imagen, borderwidth=0, highlightthickness=0)
         self.button_perfil.pack(side=tk.RIGHT, padx= 10, pady=10)

        #================Label con el nombre del usuario=======================
         self.lbl_nombre_usuario = tk.Label(self.barra_superior, text=self.usuario ,font=('Lato',15))
         self.lbl_nombre_usuario.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
         self.lbl_nombre_usuario.pack(side=tk.RIGHT, padx=5 )

         #================Boton de notificaciones==================================
         self.button_notify = tk.Button(self.barra_superior, text="\uf0f3", font=self.font_awesome,
                                       command=self.notify)
         self.button_notify.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO, bd=0)
         self.button_notify.pack(side=tk.RIGHT, padx = 5)
    
    def widgets_panel_izquierdo(self):
        #============Cerrar turno================
        self.btn_cerrar_turno = tk.Button(self.panel_izquierdo, text='Cerrar turno  \uf2f5', height=1, width=20, bd=1,
                                          command=self.cerrar_turno)
        self.btn_cerrar_turno.config( bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_cerrar_turno.pack(side=tk.TOP, pady=4, ipady=5)

        #===============botones=============================================
        self.btn_consultar_producto = tk.Button(self.panel_izquierdo, text='   \uf00d Cancelar Venta', height=1, width=20, bd=0)
        self.btn_consultar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_consultar_producto.pack(side=tk.TOP, pady=4, ipady=2)

        self.btn_registrar_producto = tk.Button(self.panel_izquierdo, text='   \uf06a Reportar', height=1, width=20, bd=0)
        self.btn_registrar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_registrar_producto.pack(side=tk.TOP, pady=4, ipady=2)
    
    def toggle_panel(self):
        if self.panel_izquierdo.winfo_ismapped():
            self.panel_izquierdo.pack_forget()
        else:
            self.panel_izquierdo.pack(side=tk.LEFT, fill='y')
    
    def notify(self):
        self.notificaciones = tk.Toplevel(self)
        self.notificaciones.geometry("400x500+900+70")
        self.notificaciones.config(bg=colores.COLOR_SEGUNDARIO)
        self.notificaciones.title("Notificaciones")
        self.notificaciones.resizable(0,0)
        self.notificaciones.grab_set()

    def cerrar_turno(self):
        respuesta = messagebox.askyesno(title='Mensaje', message='¿Quieres salir?')
        if respuesta:
            self.mostrar_login()
   
        












