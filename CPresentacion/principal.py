import tkinter as tk
import config as colores

from util.util_ventana import centrar_ventana
from util.util_imagenes import leer_imagen
from tkinter import font, messagebox, ttk

#inventario
from CPresentacion.inventario.principal_inv_consulta import InventarioConsulta
from CPresentacion.inventario.principal_inv_registrar import InventarioRegistrar
from CPresentacion.inventario.principal_inv_buscar import InventarioBuscar
from CPresentacion.inventario.principal_inv_categoira import InventarioCatalogo
#usuarios
from CPresentacion.usuarios.consultar_usuario import UsuarioConsulta
from CPresentacion.usuarios.registrar_usuario import UsuariosRegistrar

from CPresentacion.ventas.consultar_venta import VentasConsulta
from CPresentacion.home import Home

from BDominio.usuarios.cargar_usuarios import CargarUsuario

class Principal(tk.Frame):
    def __init__(self, parent, mostrar_login, mostrar_PuntoVenta, usuario):
        super().__init__(parent)
        self.place(x=0,y=0, relheight=1, relwidth=1)

        self.mostrar_login = mostrar_login
        self.mostrar_PuntoVenta = mostrar_PuntoVenta
        self.usuario = usuario
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.font_aw = font.Font(family="Font Awesome" ,size=12)

        self.paneles()
        self.widgets_barra_superior()
        self.widgets_panel_izquierdo()



    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=colores.COLOR_SEGUNDARIO, height=60)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.panel_izquierdo = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=260)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.cuerpo = tk.Frame(self, background=colores.FONDO_PRINCIPAL, bd=2)
        self.cuerpo.pack(side=tk.RIGHT, fill='both' ,expand=True)

        
    def widgets_barra_superior(self):
        self.icono = tk.Button(self.barra_superior, text= '\uf0c9', font=self.font_awesome,
                               )
        self.icono.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO, bd=0)
        self.icono.pack(side=tk.LEFT, padx=5)

        self.lbl_nombre = tk.Label(self.barra_superior, text='Quicksale', font=('Montserrat', 20))
        self.lbl_nombre.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
        self.lbl_nombre.pack(side=tk.LEFT)

        #====================crear imagen de perfil con un canvas================
        cargar_ima = CargarUsuario()
        try:
            self.imagen = leer_imagen(cargar_ima.Cargar_imagen(self.usuario), (50,40))
        except  Exception as e:
             self.imagen = leer_imagen('imagenes/sinfoto.jpg', (50,50))

        self.button_perfil = tk.Button(self.barra_superior, image=self.imagen, borderwidth=0, highlightthickness=0)
        self.button_perfil.pack(side=tk.RIGHT, padx= 10, pady=10)


        #================Label con el nombre del usuario=======================
        self.lbl_nombre_usuario = tk.Label(self.barra_superior, text=self.usuario ,font=('Lato',15))
        self.lbl_nombre_usuario.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
        self.lbl_nombre_usuario.pack(side=tk.RIGHT, padx=5 )

        #================Boton de notificaciones==================================
        self.button_notify = tk.Button(self.barra_superior, text="\uf0f3", font=self.font_awesome,
                                       )
        self.button_notify.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO, bd=0)
        self.button_notify.pack(side=tk.RIGHT, padx = 5)

    def widgets_panel_izquierdo(self):
        ancho, alto, pad, ipad = 25, 1, 4, 2

        #============Cerrar turno========
        self.btn_cerrar_turno = tk.Button(self.panel_izquierdo, text='Cerrar turno  \uf2f5', height=alto, width=ancho, bd=1,
                                          command=self.cerrar_turno)
        self.btn_cerrar_turno.config( bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_cerrar_turno.pack(side=tk.TOP, pady=pad, ipady=5)
                                         
        #======================================Home=========================================================
        self.btn_home = tk.Button(self.panel_izquierdo, text="   \uf015 Home", height=alto, width=ancho, bd=0,
                                  command=self.home)
        self.btn_home.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_home.pack(side=tk.TOP, pady=pad, ipady=ipad)

        #====================================productos====================================================
        lbl_nombre = tk.Label(self.panel_izquierdo,text='Inventario', height=alto, width=ancho, bd=0)
        lbl_nombre.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=('regular',11), anchor='w')
        lbl_nombre.pack(side=tk.TOP, pady=pad, ipady=4)

        self.btn_consultar_producto = tk.Button(self.panel_izquierdo, text='   \uf468 Consultar', height=alto, width=ancho, bd=0,
                                                command=self.inventario_consulta)
        self.btn_consultar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_consultar_producto.pack(side=tk.TOP, pady=pad, ipady=ipad)

        self.btn_registrar_producto = tk.Button(self.panel_izquierdo, text='   \uf0fe Registrar', height=alto, width=ancho, bd=0,
                                                command=self.inventario_registrar)
        self.btn_registrar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_registrar_producto.pack(side=tk.TOP, pady=pad, ipady=ipad)

        self.btn_buscar_producto = tk.Button(self.panel_izquierdo, text='   \uf002 Buscar', height=alto, width=ancho, bd=0)
        self.btn_buscar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w',
                                        command=self.inventario_buscar)
        self.btn_buscar_producto.pack(side=tk.TOP, pady=pad, ipady=ipad)


        self.btn_categoria_producto = tk.Button(self.panel_izquierdo, text="   \uf00b Categorias", height=alto, width=ancho, bd=0,
                                                command=self.inventario_catalago)
        self.btn_categoria_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_categoria_producto.pack(side=tk.TOP, pady=pad, ipady=ipad)

        #===================================Ventas=====================================================================
        lbl_ventas = tk.Label(self.panel_izquierdo,text='Ventas', height=alto, width=ancho, bd=0)
        lbl_ventas.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=('regular',11), anchor='w')
        lbl_ventas.pack(side=tk.TOP, pady=pad, ipady=4)

        self.btn_lista_ventas = tk.Button(self.panel_izquierdo, text='   \uf07a Lista de ventas', height=alto, width=ancho, bd=0,
                                          command=self.lista_venta)
        self.btn_lista_ventas.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_lista_ventas.pack(side=tk.TOP, pady=pad, ipady=ipad)

        #=====================================Usuarios========================================================================
        lbl_usuario = tk.Label(self.panel_izquierdo,text='Usuarios', height=alto, width=ancho, bd=0)
        lbl_usuario.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=('regular',11), anchor='w')
        lbl_usuario.pack(side=tk.TOP, pady=pad, ipady=4)

        self.btn_consulta_usuario = tk.Button(self.panel_izquierdo, text="   \uf007 Cosultar", height=alto, width=ancho, bd=0,
                                              command=self.usuario_consulta)
        self.btn_consulta_usuario.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_consulta_usuario.pack(side=tk.TOP, pady=pad, ipady=ipad)
        
        self.btn_registrar_usuario = tk.Button(self.panel_izquierdo, text="   \uf234 Registar", height=alto, width=ancho, bd=0,
                                            command=self.registrar_usuario)
        self.btn_registrar_usuario.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_registrar_usuario.pack(side=tk.TOP, pady=pad, ipady=ipad)

        self.btn_punto_venta = tk.Button(self.panel_izquierdo, text='Punto de venta \uf061', width=ancho, height=alto, bd=1,
                                         command=self.abrir_pos)
        self.btn_punto_venta.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_punto_venta.pack(side=tk.BOTTOM, pady=pad, ipady=5)


    def cerrar_turno(self):
        respuesta = messagebox.askyesno(title='Mensaje', message='¿Quieres salir?')
        if respuesta:
            self.mostrar_login()    
    def abrir_pos(self):
        respuesta = messagebox.askyesno('Confirmacion', '¿Quieres abril el punto de venta?')
        if respuesta:
            self.mostrar_PuntoVenta(self.usuario)
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
  
    def clear_body(self):
        for widget in self.cuerpo.winfo_children():
            widget.destroy()

    #inventario
    def inventario_consulta(self):
        self.clear_body()
        InventarioConsulta(self.cuerpo, self.inventario_registrar)
    def inventario_registrar(self):
        self.clear_body()
        InventarioRegistrar(self.cuerpo)
    def inventario_buscar(self):
        self.clear_body()
        InventarioBuscar(self.cuerpo)
    def inventario_catalago(self):
        self.clear_body()
        InventarioCatalogo(self.cuerpo)

    #Usuarios
    def usuario_consulta(self):
        self.clear_body()
        UsuarioConsulta(self.cuerpo, self.registrar_usuario)

    def registrar_usuario(self):
        self.clear_body()
        UsuariosRegistrar(self.cuerpo)
    
    def lista_venta(self):
        self.clear_body()
        VentasConsulta(self.cuerpo)

    def home(self):
        self.clear_body()
        Home(self.cuerpo)



