import tkinter as tk
import datetime
import config as colores

from tkinter import font, messagebox, ttk
from util.util_imagenes import leer_imagen

from BDominio.productos.cargar_producto import CargarProductos
from BDominio.usuarios.cargar_usuarios import CargarUsuario
from BDominio.ventas.cargar_monedas import CargarMoneda
from BDominio.productos.cargar_producto import CargarProductos
from BDominio.usuarios.validar_usuario import UsuarioValid


from BDominio.ventas.guardar_venta import Registrar_venta
from BDominio.ventas.venta_reciente import VentaReciente
from BDominio.ventas.registrar_productos_ventas import RegistrarProductoVentas
from BDominio.productos.editar_producto import EditarProducto
from BDominio.ventas.generar_factura import Factura


from util.util_ventana import centrar_ventana



class PuntoVenta(tk.Frame):
    def __init__(self, parent, mostrar_login, usuario, mostrar_principal):
        super().__init__(parent)
        self.config(background=colores.FONDO_PRINCIPAL)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_login = mostrar_login
        self.mostrar_principal = mostrar_principal
        self.usuario = usuario
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.font_aw = font.Font(family="Font Awesome" ,size=12)
        self.productos = CargarProductos()
        self.monedas = CargarMoneda()
        self.simbolo = self.monedas.cargar_simbolo_monedas('Bolivar')
        self.ultimo_texto = ''
        self.ultimo_texto2 = ''

        self.paneles()
        self.widgets_barra_superior()
        self.widgets_panel_izquierdo()
        self.widgets_list_producto()
        self.widgets_factura()
        
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=colores.COLOR_SEGUNDARIO, height=60)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.panel_izquierdo = tk.Frame(self, bg=colores.COLOR_PRINCIPAL, width=190)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.factura = tk.Frame(self, bg=colores.FONDO_PRINCIPAL, width=480)
        self.factura.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True ,padx=5, pady=5)

        self.list_productos = tk.Frame(self, bg=colores.BOTON_PRODUCTOS, width=667)
        self.list_productos.pack(side=tk.RIGHT, fill=tk.BOTH , expand=True, padx=1, pady=5)

        
    #=============Creacion de widgets=================================
    def widgets_barra_superior(self):
         self.icono = tk.Button(self.barra_superior, text= '\uf0c9', font=self.font_awesome,
                               )
         self.icono.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO, bd=0)
         self.icono.pack(side=tk.LEFT, padx=5)

         self.lbl_nombre = tk.Label(self.barra_superior, text='Quicksale', font=('Montserrat', 20))
         self.lbl_nombre.config(bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
         self.lbl_nombre.pack(side=tk.LEFT)

         #====================crear imagen de perfil con un canvas================

         cargar_imag = CargarUsuario()
         try:
            self.imagen = leer_imagen(cargar_imag.Cargar_imagen(self.usuario), (50,40))
         except Exception as e:
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
        #============Cerrar turno================
        self.btn_cerrar_turno = tk.Button(self.panel_izquierdo, text='Cerrar turno  \uf2f5', height=1, width=20, bd=1,
                                          command=self.cerrar_turno)
        self.btn_cerrar_turno.config( bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_cerrar_turno.pack(side=tk.TOP, pady=4, ipady=5)

        #===============botones=============================================
        '''self.btn_consultar_producto = tk.Button(self.panel_izquierdo, text='   \uf00d Cancelar Venta', height=1, width=20, bd=0)
        self.btn_consultar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_consultar_producto.pack(side=tk.TOP, pady=4, ipady=2)

        self.btn_reportar_producto = tk.Button(self.panel_izquierdo, text='   \uf06a Reportar', height=1, width=20, bd=0)
        self.btn_reportar_producto.config(bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
        self.btn_reportar_producto.pack(side=tk.TOP, pady=4, ipady=2)'''

        admin = UsuarioValid()
        acceso = admin.acceso(self.usuario)

        if acceso == 2:
            self.btn_ir_principal = tk.Button(self.panel_izquierdo, text='Gestion  \uf859', height=1, width=20, bd=1,
                                          command=self.ir_principal)
            self.btn_ir_principal.config( bg = colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO, font=self.font_aw, anchor='w')
            self.btn_ir_principal.pack(side=tk.BOTTOM, pady=4, ipady=5)
    def widgets_factura(self):
        self.productos_factura = []
        #=====================frame titulo==============================
        self.frame_titulo = tk.Frame(self.factura, bg=colores.FONDO_SEGUNDARIO)
        self.frame_titulo.place(x=2, y=2, relwidth=0.99, height=50)

        lbl_titulo = tk.Label(self.frame_titulo, text="Factura de venta", font='Roboto 12 bold', bg=colores.FONDO_SEGUNDARIO)
        lbl_titulo.place(x=10, y=15)

        #===================frmae especificaciones==============================
        self.frame_especificaciones = tk.Frame(self.factura, bg = colores.FONDO_SEGUNDARIO)
        self.frame_especificaciones.place(x=2, y=50, relwidth=0.99, height=115)
        
        moneda = self.monedas.cargar_nombres_monedas()

        lbl_moneda = tk.Label(self.frame_especificaciones, text='Moneda', font='roboto 12' ,bg=colores.FONDO_SEGUNDARIO)
        lbl_moneda.grid(row=0, column=0, pady=10, padx=18)

        self.combo_moneda = ttk.Combobox(self.frame_especificaciones, values=moneda ,font='roboto 12', background=colores.FONDO_SEGUNDARIO)
        self.combo_moneda.grid(row=0, column=1, pady=10, padx=10, ipady=6, ipadx=75, columnspan=2, sticky=tk.W)
        self.combo_moneda.current(0)

        lbl_cambio = tk.Label(self.frame_especificaciones, text='Cambio', font='roboto 12' ,bg=colores.FONDO_SEGUNDARIO)
        lbl_cambio.grid(row=1, column=0, pady=10, padx=18)

        self.cambio_moneda = ttk.Combobox(self.frame_especificaciones, values=moneda ,font='roboto 12', background=colores.FONDO_SEGUNDARIO)
        self.cambio_moneda.grid(row=1, column=1, pady=10, padx=10, ipady=6, ipadx=75, columnspan=2, sticky=tk.W)
        self.cambio_moneda.current(0)

        #====================frame productos factura===============================================================
        self.frame_productos_factura = tk.Frame(self.factura, bg=colores.FONDO_SEGUNDARIO)
        self.frame_productos_factura.place(x=2, y=165, relwidth=0.99, height=350)
        
        self.canvas2 = tk.Canvas(self.frame_productos_factura)
        scrollbar = ttk.Scrollbar(self.frame_productos_factura, orient='vertical', command=self.canvas2.yview)
        self.scrollable_productos = tk.Frame(self.canvas2, bg="white")
        
        self.scrollable_productos.bind("<Configure>", lambda e: self.canvas2.configure(scrollregion=self.canvas2.bbox("all")))
        
        window_frame = self.canvas2.create_window((0, 0), window=self.scrollable_productos, anchor='nw')
        self.canvas2.configure(yscrollcommand=scrollbar.set)
        
        self.canvas2.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        #===================frame botonees =======================================================================
        self.frame_botones = tk.Frame(self.factura, bg=colores.FONDO_SEGUNDARIO)
        self.frame_botones.place(x=0, y=515, relheight=0.99, relwidth=0.99)

        self.boton_pagar = tk.Button(self.frame_botones, text='Vender', bg=colores.BOTON_PRODUCTOS, font='roboto 12', width=20, anchor='w',
                                     command=self.vender)
        self.boton_pagar.grid(row=0, column=0, padx=5 ,pady=5, ipadx=45, ipady=4)

        self.entry_precio_pagar = ttk.Entry(self.frame_botones, font='Roboto 12', width=20, justify='right', background=colores.BOTON_PRODUCTOS)
        self.entry_precio_pagar.grid(row=0, column=1, pady=5 ,ipady=7)
        self.entry_precio_pagar.config(state=tk.DISABLED)

        self.boton_cancelar = tk.Button(self.frame_botones, text='cancelar', bg=colores.BOTON_PRODUCTOS, font='roboto 12',  width=20, anchor='w', 
                                        command=self.cancelar_factura)
        self.boton_cancelar.grid(row=1, column=0, padx=5 ,pady=5, ipadx=45, ipady=4)

        self.entry_productos_pagar = ttk.Entry(self.frame_botones, font='Roboto 12',  width=20, justify='right', background=colores.BOTON_PRODUCTOS)
        self.entry_productos_pagar.grid(row=1, column=1, pady=5 ,ipady=7)
        self.entry_productos_pagar.config(state=tk.DISABLED)
    def widgets_list_producto(self):
        #================frame buscar==========================================================
        self.frame_buscar = tk.Frame(self.list_productos, bg=colores.FONDO_SEGUNDARIO)
        self.frame_buscar.place(x=0, y=0, relwidth=1, height=145)

        lbl_producto = tk.Label(self.frame_buscar, text=' \uf468 Productos', font=self.font_aw, bg=colores.FONDO_SEGUNDARIO)
        lbl_producto.grid(row=0, column=0, ipadx=10, pady=5,columnspan=3)
        
        barra = tk.Label(self.frame_buscar, font=self.font_aw)
        barra.grid(row=1, column=0, ipadx=1, ipady=2 ,sticky=tk.E)

        self.boton_codigo_barra = tk.Button(self.frame_buscar, text='\uf468', font=self.font_aw, bg=colores.BOTON_PRODUCTOS)
        self.boton_codigo_barra.grid(row=1, column=1, ipadx=15, ipady=3 ,sticky=tk.E)

        self.boton_buscar = tk.Button(self.frame_buscar, text='\uf002', font=self.font_aw, bg=colores.BOTON_PRODUCTOS,
                                      command=self.buscar_producto)
        self.boton_buscar.grid(row=1, column=2,ipadx=15, ipady=3 ,sticky=tk.E)

        self.entry_codigo_barra = ttk.Entry(self.frame_buscar, font='roboto 12')
        self.entry_codigo_barra.grid(row=1, column=3 ,ipady=6, ipadx=170, sticky=tk.E)
        self.entry_codigo_barra.bind("<KeyRelease>", self.detectar_eliminacion_codigo_barra)

        label_buscar = tk.Label(self.frame_buscar, text='Buscar', font='Roboto 12', bg=colores.FONDO_SEGUNDARIO)
        label_buscar.grid(row=2, column=3, pady=10, ipadx=15, ipady=3)

        self.entry_buscar = ttk.Entry(self.frame_buscar, font='roboto 12')
        self.entry_buscar.grid(row=2, column=3, pady=15 ,ipady=6, ipadx=10, sticky=tk.E)
        self.entry_buscar.bind("<KeyRelease>", self.detectar_eliminacion)

        self.create_scrollable_list()

    #================lista de productos=====================================================
    def create_scrollable_list(self):
        container = tk.Frame(self.list_productos, bd=0.5)
        container.place(x=0, y=145, relheight=0.8, relwidth=1)

        # Crear encabezados
        header_frame = tk.Frame(container, bg=colores.BOTON_PRODUCTOS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Id", width=17,height=2 ,anchor='center',  bg=colores.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Descripcion", width=20, height=2 ,anchor='center',  bg=colores.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text=f'Precio {self.simbolo['Bolivar']}', width=17,height=2 ,anchor='center',  bg=colores.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Cantidad", width=17,height=2 ,anchor='center',  bg=colores.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Opciones", width=17,height=2 ,anchor='w',  bg=colores.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        
        self.canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        window_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.populate_list()   
    def populate_list(self):
        #Datos de productos
        productos = CargarProductos()
        data = productos.cargar_productos_activos()

        si = 0
        
        for item in data:            
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0
            estado = 'green' if item['estado'] else 'red'

            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill='x', pady=3)
            
            tk.Label(row_frame, text=item['id'], width=17, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['desc']}", width=20, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['precio']}", width=17, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['cantidad']}", width=17, anchor='center', bg=c).pack(side='left', padx=5)
            
            tk.Button(row_frame, text="Agregar", width=10, bg=colores.BOTON_PRODUCTOS, bd = 0,
                      command=lambda e = item: self.agregar(e)).pack(side='left', padx=6, ipady=2, pady=7)         


    #================buscar productos==============================================================
    def populate_list_busqueda(self, datos):
        #Datos de productos
        data = datos

        si = 0
        
        for item in data:            
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0
            estado = 'green' if item['estado'] else 'red'

            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill='x', pady=3)
            
            tk.Label(row_frame, text=item['id'], width=17, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['desc']}", width=20, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['precio']}", width=17, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['cantidad']}", width=17, anchor='center', bg=c).pack(side='left', padx=5)
            
            tk.Button(row_frame, text="Agregar", width=10, bg=colores.BOTON_PRODUCTOS, bd = 0,
                      command=lambda e = item :self.agregar(e)).pack(side='left', padx=6, ipady=2, pady=7)
    def buscar_producto(self):
        if len(self.entry_codigo_barra.get()) == 0:
            messagebox.showerror('Error', 'Campo de busqueda vacio')
            return
        busqueda = self.productos.buscar_producto_id_activo(self.entry_codigo_barra.get())
        if busqueda == False:
            messagebox.showerror('Error', 'Datos incorrectos')
            return
        self.update_lista_busqueda(busqueda)
    def buscar_producto_desc(self):
        busqueda = self.productos.buscar_producto_desc_activo(self.entry_buscar.get())
        if busqueda == False:
            messagebox.showerror('Error', 'Datos incorrectos')
            return
        self.update_lista_busqueda(busqueda)
    def detectar_eliminacion(self,event):
        texto_actual = self.entry_buscar.get()

        # Verifica si se eliminó texto (comparando la longitud)
        if len(texto_actual) < len(self.ultimo_texto):
            if len(texto_actual) == 0:
                self.update_lista_busqueda(self.productos.cargar_productos_activos())
            else:
                self.buscar_producto_desc()
        elif len(texto_actual) > len(self.ultimo_texto):
            if len(texto_actual) == 0:
                self.update_lista_busqueda(self.productos.cargar_productos_activos())
            else :
                self.buscar_producto_desc()  

        #Actualizar el último estado del texto
        self.ultimo_texto = texto_actual
    def detectar_eliminacion_codigo_barra(self,event):
        texto_actual = self.entry_codigo_barra.get()

        # Verifica si se eliminó texto (comparando la longitud)
        if len(texto_actual) < len(self.ultimo_texto2):
            if len(texto_actual) == 0:
                self.update_lista_busqueda(self.productos.cargar_productos_activos())
            else:
                self.buscar_producto()
        elif len(texto_actual) > len(self.ultimo_texto2):
            if len(texto_actual) == 0:
                self.update_lista_busqueda(self.productos.cargar_productos_activos())
            else:
                self.buscar_producto()
        
        # Actualizar el último estado del texto
        self.ultimo_texto2 = texto_actual
    def update_lista_busqueda(self, data):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.populate_list_busqueda(data)


    #==================Agregar producto a facturaa==============================================================
    def agregar(self, item):
        id = item['id']
        descripcion = item['desc']
        precio = item['precio']

        if self.verificar_existencia(id):
            for producto in self.productos_factura:
                if producto['id'] == id:
                   
                   if item['cantidad'] <= producto['cantidad']:
                       messagebox.showinfo('Mensaje', 'Producto agotado')
                       return 0
                   
                   producto['cantidad'] += 1
                   self.actualizar_cantidad_factura(id)
                   self.aumentar_cantidad_producto()
                   self.aumentar_precio_venta(precio)
        else:
            if item['cantidad'] < 1:
                messagebox.showinfo('Mensaje', 'Producto agotado')
                return 0

            producto_dic = {'id' : id, 'desc' : descripcion, 'precio' : precio, 'cantidad' : 1, 'cant' : item['cantidad']}
            self.productos_factura.append(producto_dic)
            self.agregar_a_factura(producto_dic)
            self.aumentar_cantidad_producto()
            self.aumentar_precio_venta(precio)
    def agregar_a_factura(self, producto):
        frame_producto = tk.Frame(self.scrollable_productos)
        frame_producto.pack(fill='x', pady=3)

        lbl_id = tk.Label(frame_producto, text=f'{producto['id']}', anchor='w', justify='left')

        des = tk.Label(frame_producto, text=f'{producto['desc']}\n{producto['precio']}', width=20, anchor='w', justify='left').pack(side='left', padx=5)

        mas = tk.Button(frame_producto, text = '+'  , anchor='center', font='roboto 14', bd=0, 
                       command=lambda c = producto['id'], ca = producto['cant']: self.aumentar_cantidad_boton(c, ca)).pack(side='left', padx=5)
        
        cant = tk.Label(frame_producto, text='1', width=10, anchor='center').pack(side='left', padx=5)

        menos = tk.Button(frame_producto, text = '-' , anchor='center',  font='roboto 14', bd=0,
                          command= lambda c = producto['id'] : self.disminuir_cantidad_boton(c)).pack(side='left', padx=5)


        precio = tk.Label(frame_producto, text=f'{producto['precio'] }', width=18, anchor='e', ).pack(side='left', padx=5)
        simbolo = tk.Label(frame_producto, text=self.simbolo[self.combo_moneda.get()], width=2, anchor='e', ).pack(side='left')
    def verificar_existencia(self, id):
        if self.productos_factura == None:
            return False
        for producto in self.productos_factura:
            if producto['id'] == id:
                return True
        return False
    

    def actualizar_cantidad_factura(self, codigo):
        precio1 = ''
        for frame_producto_factura in self.scrollable_productos.winfo_children():
            for j, producto in enumerate(frame_producto_factura.winfo_children()):
                if isinstance(producto, tk.Label):
                    if j == 0:
                        if str(codigo) != producto.cget('text'):
                            break
                    elif j == 1:
                        descripcion, precio1 = producto.cget('text').split("\n")
                        precio1 = float(precio1)
                    elif j == 3 :
                        cantidad = int(producto.cget('text'))
                        producto.config(text=f'{cantidad + 1}')
                    elif j == 5:
                        precio_total = float(producto.cget('text'))
                        precio_total = precio_total + precio1
                        producto.config(text=f'{precio_total}')
                        return

    def aumentar_cantidad_boton(self, codigo, cantidad_producto):
        precio1 = ''
        for frame_producto_factura in self.scrollable_productos.winfo_children():
            for j, producto in enumerate(frame_producto_factura.winfo_children()):
                if isinstance(producto, tk.Label):
                    if j == 0:
                        if str(codigo) != producto.cget('text'):
                            break
                    elif j == 1:
                        descripcion, precio1 = producto.cget('text').split("\n")
                        precio1 = float(precio1)
                    elif j == 3 :
                        cantidad = int(producto.cget('text'))
                        if cantidad >= cantidad_producto:
                            messagebox.showinfo('Mensaje', 'Producto agotado')
                            return
                        producto.config(text=f'{cantidad + 1}')
                        for producto in self.productos_factura:
                            if producto['id'] == codigo:
                                producto['cantidad'] += 1
                        self.aumentar_cantidad_producto()
                        self.aumentar_precio_venta(precio1)
                    elif j == 5:
                        precio_total = float(producto.cget('text'))
                        precio_total = precio_total + precio1
                        producto.config(text=f'{precio_total}')
                        return                 
    def disminuir_cantidad_boton(self, codigo):
        precio1 = ''
        for frame_producto_factura in self.scrollable_productos.winfo_children():
            for j, producto in enumerate(frame_producto_factura.winfo_children()):
                if isinstance(producto, tk.Label):
                    if j == 0:
                        if str(codigo) != producto.cget('text'):
                            break
                    elif j == 1:
                        descripcion, precio1 = producto.cget('text').split("\n")
                        precio1 = float(precio1)
                    elif j == 3 :
                        cantidad = int(producto.cget('text'))
                        if cantidad == 1: 
                           frame_producto_factura.destroy()
                           productos_filtrados = [d for d in self.productos_factura if d['id'] != codigo]
                           self.productos_factura = productos_filtrados
                           self.disminuir_cantidad_producto()
                           self.disminuir_precio_pagar(precio1)
                           return
                        else:
                            producto.config(text=f'{cantidad - 1}')
                            for producto in self.productos_factura:
                                if producto['id'] == codigo:
                                    producto['cantidad'] -=1
                            self.disminuir_cantidad_producto()

                    elif j == 5:
                        precio_total = float(producto.cget('text'))
                        precio_total = precio_total - precio1
                        producto.config(text=f'{precio_total}')
                        self.disminuir_precio_pagar(precio1)
                        return                   
    def actualizar_cantidad_factura(self, codigo):
        precio1 = ''
        for frame_producto_factura in self.scrollable_productos.winfo_children():
            for j, producto in enumerate(frame_producto_factura.winfo_children()):
                if isinstance(producto, tk.Label):
                    if j == 0:
                        if str(codigo) != producto.cget('text'):
                            break
                    elif j == 1:
                        descripcion, precio1 = producto.cget('text').split("\n")
                        precio1 = float(precio1)
                    elif j == 3 :
                        cantidad = int(producto.cget('text'))
                        producto.config(text=f'{cantidad + 1}')
                    elif j == 5:
                        precio_total = float(producto.cget('text'))
                        precio_total = precio_total + precio1
                        producto.config(text=f'{precio_total}')
                        return         
    def aumentar_cantidad_producto(self):
        self.entry_productos_pagar.config(state=tk.NORMAL)
        if len(self.entry_productos_pagar.get()) == 0:
            self.entry_productos_pagar.insert(0, '1')
        else:
            cantidad = int(self.entry_productos_pagar.get())
            self.entry_productos_pagar.delete(0, 'end')
            self.entry_productos_pagar.insert(0, f'{1 + cantidad}')
        self.entry_productos_pagar.config(state=tk.DISABLED)
    def aumentar_precio_venta(self, precio):
        self.entry_precio_pagar.config(state=tk.NORMAL)
        if len(self.entry_precio_pagar.get()) == 0:
            self.entry_precio_pagar.insert(0, f'{precio}')
        else:
            cantidad = float(self.entry_precio_pagar.get())
            self.entry_precio_pagar.delete(0, 'end')
            self.entry_precio_pagar.insert(0, f'{precio + cantidad}')
        self.entry_precio_pagar.config(state=tk.DISABLED)  
    def disminuir_cantidad_producto(self):
        self.entry_productos_pagar.config(state=tk.NORMAL)
        cantidad = int(self.entry_productos_pagar.get())
        self.entry_productos_pagar.delete(0, 'end')
        self.entry_productos_pagar.insert(0, f'{cantidad - 1}')
        self.entry_productos_pagar.config(state=tk.DISABLED)
    def disminuir_precio_pagar(self, precio):
        self.entry_precio_pagar.config(state=tk.NORMAL)
        cantidad = float(self.entry_precio_pagar.get())
        self.entry_precio_pagar.delete(0, 'end')
        self.entry_precio_pagar.insert(0, f'{cantidad - precio}')
        self.entry_precio_pagar.config(state=tk.DISABLED) 
    def cancelar_factura(self):
        if messagebox.askretrycancel('Mensaje','¿Cancelar factura?'):
            for frame in self.scrollable_productos.winfo_children():
                frame.destroy()
            self.entry_precio_pagar.config(state=tk.NORMAL)
            self.entry_productos_pagar.config(state=tk.NORMAL)
            self.entry_precio_pagar.delete(0, 'end')
            self.entry_productos_pagar.delete(0, 'end')
            self.entry_precio_pagar.config(state=tk.DISABLED)
            self.entry_productos_pagar.config(state=tk.DISABLED)
            self.productos_factura = []
            

    def limpiar_despues_venta(self):
       for frame in self.scrollable_productos.winfo_children():
            frame.destroy()
       self.entry_precio_pagar.config(state=tk.NORMAL)
       self.entry_productos_pagar.config(state=tk.NORMAL)
       self.entry_precio_pagar.delete(0, 'end')
       self.entry_productos_pagar.delete(0, 'end')
       self.entry_precio_pagar.config(state=tk.DISABLED)
       self.entry_productos_pagar.config(state=tk.DISABLED)
       self.productos_factura = []
       for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
       self.populate_list()

    #================funciones cobrar o vender===================================
    def vender(self):
        c = 0 if len(self.entry_productos_pagar.get()) == 0 else int(self.entry_productos_pagar.get())
        if c == 0:
            return 0 

        PagarFactura(self, self.productos_factura, float(self.entry_precio_pagar.get()), float(self.entry_productos_pagar.get()), self.simbolo, self.limpiar_despues_venta)

    #================configuraciones de punto de venta================================== 
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
   
    def ir_principal(self):
        if messagebox.askyesno(title='Mensaje', message='¿Quieres volver?'):
            self.mostrar_principal(self.usuario)




class PagarFactura(tk.Toplevel):
    def __init__(self, parent, productos, precio_total, n_producto, moneda, limpiar_despues_de_venta):
        super().__init__(parent)
        self.title('Pago factura')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=colores.FONDO_SEGUNDARIO)
        

        self.productos = productos
        self.n_producto = n_producto
        self.precio_total = precio_total
        self.moneda = moneda
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.limpiar_despues_de_venta = limpiar_despues_de_venta
        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = tk.Label(self, text='Pagar factura', font='roboto 16', bg=colores.FONDO_SEGUNDARIO)
        lbl_titulo.pack(pady=10, padx=20)

        lbl_precio_total = tk.Label(self, text='Total', font='roboto 14', bg=colores.FONDO_SEGUNDARIO)
        lbl_precio_total.pack(pady=5)

        lbl_precio = tk.Label(self, text=f'{self.moneda['Bolivar']} {self.precio_total}',font = 'roboto 16', bg=colores.FONDO_SEGUNDARIO, fg=colores.COLOR_FACTURA)
        lbl_precio.pack(pady=5)

        self.frame_metodo = tk.LabelFrame(self, text='Metodo de pago',  font='roboto 11', bg=colores.FONDO_SEGUNDARIO)
        self.frame_metodo.pack(pady=15, padx=60)

        self.boton_efectivo = tk.Button(self.frame_metodo, text='Efectivo\n\uf0d6', justify='center', font=self.font_awesome, fg=colores.COLOR_FACTURA,
        command=self.pagar_efectivo)
        self.boton_efectivo.pack(pady=15, padx=60)

        self.boton_tarjeta = tk.Button(self.frame_metodo, text='Tarjeta \n\uf09d', justify='center', font=self.font_awesome, fg=colores.COLOR_FACTURA,
                                       command=self.pagar_banco)
        self.boton_tarjeta.pack(pady=15, padx=60)

        self.boton_cancelar = tk.Button(self, text='Cancelar', font='roboto 12', bg=colores.FONDO_SEGUNDARIO,
                                        command=self.destroy)
        self.boton_cancelar.pack(anchor='e', padx=10, pady=10)
        
    def pagar_efectivo(self):
        PagarEfectivo(self, self.productos, self.precio_total, self.n_producto, self.moneda['Bolivar'], self.limpiar_despues_de_venta)
    def pagar_banco(self):
        PagarBanco(self, self.productos, self.precio_total, self.n_producto, self.moneda['Bolivar'], self.limpiar_despues_de_venta)


class PagarEfectivo(tk.Toplevel):
    def __init__(self, parent, productos, precio_total, n_producto, moneda, limpiar_despues_de_venta):
        super().__init__(parent)
        self.title('Pagar efectivo')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=colores.FONDO_SEGUNDARIO)
        self.ultimo_texto = ''

        self.productos = productos
        self.n_producto = n_producto
        self.precio_total = precio_total
        self.moneda = moneda
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.parent = parent
        self.limpiar_despues_de_venta = limpiar_despues_de_venta

        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = tk.Label(self, text='Pagar efectivo', font='roboto 16', bg=colores.FONDO_SEGUNDARIO)
        lbl_titulo.pack(pady=10, padx=20)

        lbl_precio_total = tk.Label(self, text='Total', font='roboto 14', bg=colores.FONDO_SEGUNDARIO)
        lbl_precio_total.pack(pady=5)

        lbl_precio = tk.Label(self, text=f'{self.moneda} {self.precio_total}',font = 'roboto 16', bg=colores.FONDO_SEGUNDARIO, fg=colores.COLOR_FACTURA)
        lbl_precio.pack(padx=10, pady=5)

        self.frame_metodo = tk.LabelFrame(self, text='Efectivo',  font='roboto 11', bg=colores.FONDO_SEGUNDARIO)
        self.frame_metodo.pack(pady=15, padx=60)

        lbl_pago = tk.Label(self.frame_metodo, text='Pago en efectivo',font = 'roboto 12', bg=colores.FONDO_SEGUNDARIO, justify='left')
        lbl_pago.pack(padx=10,ipady=9, anchor='w')

        self.entry_pago_efectivo = ttk.Entry(self.frame_metodo,font='roboto 12' )
        self.entry_pago_efectivo.pack(pady=5, ipadx=80, ipady=10)
        self.entry_pago_efectivo.bind("<KeyRelease>", self.detectar_eliminacion)
    

        lbl_cambio = tk.Label(self.frame_metodo, text='Cambio',font = 'roboto 12', bg=colores.FONDO_SEGUNDARIO, justify='left')
        lbl_cambio.pack(padx=10 ,ipady=9, anchor='w')
        
        self.entry_cambio_efectivo = ttk.Entry(self.frame_metodo, font='roboto 12')
        self.entry_cambio_efectivo.pack( pady=5 ,padx=20, ipadx=80, ipady=10)
        self.entry_cambio_efectivo.config(state=tk.DISABLED)


        self.boton_pagar = tk.Button(self, text='Pagar', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                        command=self.vender)
        self.boton_pagar.pack( padx=70, pady=6, fill='x', expand=True, ipady=8)

        self.boton_cancelar = tk.Button(self, text='Cancelar', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                 command=self.destroy)
        self.boton_cancelar.pack(padx=70, pady=6, fill='x', expand=True, ipady=8)
    
    def detectar_eliminacion(self,event):
        texto_actual = self.entry_pago_efectivo.get()
        
        # Verifica si se eliminó texto (comparando la longitud)
        self.entry_cambio_efectivo.config(state=tk.NORMAL)
        try:
            if len(texto_actual) < len(self.ultimo_texto):
                if len(texto_actual) == 0:
                    self.entry_cambio_efectivo.delete(0, 'end')
                else:
                    cantidad = float(self.entry_pago_efectivo.get())
                    self.entry_cambio_efectivo.delete(0, 'end')
                    self.entry_cambio_efectivo.insert(0, f'{self.precio_total - cantidad}')
            else:
                if len(texto_actual)== 0:
                    self.entry_cambio_efectivo.delete(0, 'end')
                else:
                    
                    cantidad = float(self.entry_pago_efectivo.get())
                    self.entry_cambio_efectivo.delete(0, 'end')
                    self.entry_cambio_efectivo.insert(0, f'{self.precio_total - cantidad}')
        except Exception as e:
            messagebox.showerror('Error', 'Ingrese sol0 numeros', parent = self)

        self.entry_cambio_efectivo.config(state=tk.DISABLED)
                
        # Actualizar el último estado del texto
        self.ultimo_texto = texto_actual

    def vender(self):
        if not messagebox.askyesno('Mensaje', '¿Vender producto?', parent = self):
            return 0
        
        fecha_hora = datetime.datetime.now()
        registar_ven = Registrar_venta()
        monedas = CargarMoneda()
        moneda = monedas.cargar_nombre_monedas(self.moneda)

        fecha, hora = fecha_hora.date(), fecha_hora.strftime("%H:%M:%S")

        if not registar_ven.guardar_venta(self.precio_total, fecha, moneda, hora):
            print(self.precio_total,fecha,moneda,hora)
            messagebox.showerror('Error','No se pudo hacer la venta error al guardar los datos')
            return 0 
        
        cargar_id_venta = VentaReciente()
        id_venta = cargar_id_venta.venta_reciente(fecha, hora, self.precio_total)

        if id_venta == False or id_venta == None:
            messagebox.showerror('Error','No se pudo cargar el id venta')
            return 0
        
        registrar_producto_venta = RegistrarProductoVentas()
      
        if not registrar_producto_venta.registrar_producto_venta(id_venta, self.productos):
            messagebox.showerror('Error', 'No se pudo registrar los producto ventas')
            return 0
        
        disminuir_productos = EditarProducto()

        if not disminuir_productos.disminuir_producto(self.productos):
            messagebox.showerror('Error', 'Al disminuir los productos')
            return 0
        
        Imprimir_factura(self,id_venta, self.moneda, self.precio_total, self.parent, self.limpiar_despues_de_venta)
       

class PagarBanco(tk.Toplevel):
    def __init__(self, parent, productos, precio_total, n_producto, moneda, limpiar_despues_de_venta):
        super().__init__(parent)
        self.title('Pagar banco')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=colores.FONDO_SEGUNDARIO)
        self.ultimo_texto = ''

        self.productos = productos
        self.n_producto = n_producto
        self.precio_total = precio_total
        self.moneda = moneda
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=20)
        self.parent = parent
        self.limpiar_despues_de_venta = limpiar_despues_de_venta

        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = tk.Label(self, text='Pagar Banco', font='roboto 16', bg=colores.FONDO_SEGUNDARIO)
        lbl_titulo.pack(pady=10, padx=20)

        lbl_precio_total = tk.Label(self, text='Total', font='roboto 14', bg=colores.FONDO_SEGUNDARIO)
        lbl_precio_total.pack(pady=5)

        lbl_precio = tk.Label(self, text=f'{self.moneda} {self.precio_total}',font = 'roboto 16', bg=colores.FONDO_SEGUNDARIO, fg=colores.COLOR_FACTURA)
        lbl_precio.pack(padx=10, pady=5)

        self.frame_metodo = tk.LabelFrame(self, text='Bancos',  font='roboto 11', bg=colores.FONDO_SEGUNDARIO)
        self.frame_metodo.pack(pady=15, padx=60)

        lbl_pago = tk.Label(self.frame_metodo, text='Precio a pagar',font = 'roboto 12', bg=colores.FONDO_SEGUNDARIO, justify='left')
        lbl_pago.pack(padx=10,ipady=9, anchor='w')

        self.entry_pago_efectivo = ttk.Entry(self.frame_metodo,font='roboto 12' )
        self.entry_pago_efectivo.pack(pady=5, ipadx=80, ipady=10) 
        self.entry_pago_efectivo.insert(0, self.precio_total)
        self.entry_pago_efectivo.config(state=tk.DISABLED)   

        lbl_cambio = tk.Label(self.frame_metodo, text='Cambio',font = 'roboto 12', bg=colores.FONDO_SEGUNDARIO, justify='left')
        lbl_cambio.pack(padx=10 ,ipady=9, anchor='w')
        
        self.entry_cambio_efectivo = ttk.Combobox(self.frame_metodo, font='roboto 12', values=('Banco venezuela', 'Banco banesco'))
        self.entry_cambio_efectivo.pack( pady=5 ,padx=20, ipadx=75, ipady=10)

        self.boton_pagar = tk.Button(self, text='Pagar', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                        command=self.vender)
        self.boton_pagar.pack( padx=70, pady=6, fill='x', expand=True, ipady=8)

        self.boton_cancelar = tk.Button(self, text='Cancelar', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                 command=self.destroy)
        self.boton_cancelar.pack(padx=70, pady=6, fill='x', expand=True, ipady=8)

    def vender(self):
        if not messagebox.askyesno('Mensaje', '¿Vender productos?', parent = self):
            return 0
        
        fecha_hora = datetime.datetime.now()
        registar_ven = Registrar_venta()
        monedas = CargarMoneda()
        moneda = monedas.cargar_nombre_monedas(self.moneda)

        fecha, hora = fecha_hora.date(), fecha_hora.strftime("%H:%M:%S")

        if not registar_ven.guardar_venta(self.precio_total, fecha, moneda, hora):
            print(self.precio_total,fecha,moneda,hora)
            messagebox.showerror('Error','No se pudo hacer la venta error al guardar los datos')
            return 0 
        
        cargar_id_venta = VentaReciente()
        id_venta = cargar_id_venta.venta_reciente(fecha, hora, self.precio_total)

        if id_venta == False or id_venta == None:
            messagebox.showerror('Error','No se pudo cargar el id venta')
            return 0
        
        registrar_producto_venta = RegistrarProductoVentas()
      
        if not registrar_producto_venta.registrar_producto_venta(id_venta, self.productos):
            messagebox.showerror('Error', 'No se pudo registrar los producto ventas')
            return 0
        
        disminuir_productos = EditarProducto()

        if not disminuir_productos.disminuir_producto(self.productos):
            messagebox.showerror('Error', 'Al disminuir los productos')
            return 0
        
        Imprimir_factura(self, id_venta, self.moneda, self.precio_total, self.parent, self.limpiar_despues_de_venta)
        


class Imprimir_factura(tk.Toplevel):
    def __init__(self, parent, id_venta, moneda, precio, abuelo, limpiar_factura):
        super().__init__(parent)
        self.title('Factura')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=colores.FONDO_SEGUNDARIO)
        self.ultimo_texto = ''

        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=35)
        self.parent = parent

        self.id_venta = id_venta
        self.moneda = moneda
        self.precio_total = precio
        self.abuelo = abuelo
        self.limpiar_factura =limpiar_factura

        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = tk.Label(self, text='Factura', font='roboto 16', bg=colores.FONDO_SEGUNDARIO)
        lbl_titulo.pack(pady=10, padx=20)

        lbl_icono = tk.Label(self, text='\uf058', font=self.font_awesome, bg=colores.FONDO_SEGUNDARIO)
        lbl_icono.pack(pady=5, padx=10)

        lbl_bien = tk.Label(self, text='Muy bien', font='roboto 12', bg=colores.FONDO_SEGUNDARIO)
        lbl_bien.pack(pady=5)

        lbl_bien_venta = tk.Label(self, text='La venta se guardo con exito', font='roboto 12', bg=colores.FONDO_SEGUNDARIO)
        lbl_bien_venta.pack(pady=5)

        self.frame_metodo = tk.Frame(self, bg=colores.FONDO_SEGUNDARIO)
        self.frame_metodo.pack(pady=15, padx=60)

        lbl_precio_total = tk.Label(self.frame_metodo, text='Total', font='roboto 16', bg=colores.FONDO_SEGUNDARIO)
        lbl_precio_total.pack(side='left',pady=5)

        lbl_precio = tk.Label(self.frame_metodo, text=f'{self.moneda} {self.precio_total}',font = 'roboto 16', bg=colores.FONDO_SEGUNDARIO, fg=colores.COLOR_FACTURA)
        lbl_precio.pack(side='right',padx=15, pady=5)

        self.imprimir = tk.Button(self, text='Imprimir', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                        command=self.imprimir_factura)
        self.imprimir.pack( padx=60, pady=6, fill='x', expand=True, ipady=8)

        self.nueva_venta = tk.Button(self, text='Nueva venta', font='roboto 12', bg=colores.COLOR_FACTURA, bd=0,
                                 command=self.nueva_venta)
        self.nueva_venta.pack(padx=70, pady=6, fill='x', expand=True, ipady=8)

    def imprimir_factura(self):
        factura = Factura(self.id_venta)
        factura.vista_previa()

    def nueva_venta(self):
        self.limpiar_factura()
        self.abuelo.destroy()



