import tkinter as tk
import config as color

from tkinter import ttk, messagebox, font

from CPresentacion.inventario.principal_inv_editar import EditarProductoTop
from CPresentacion.inventario.principal_inv_reponer import ReponerProductoTop

from BDominio.productos.cargar_producto import CargarProductos
from BDominio.productos.eliminar_producto import EliminarProducto

from util.util_imagenes import leer_imagen


class InventarioBuscar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)
        self.ultimo_texto = ''
        self.productos = CargarProductos()

        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)
        font_aw = font.Font(family="Font Awesome" ,size=15)

        lbl_inventario = tk.Label(self, text='Inventario/Buscar', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Buscar productos \uf002", font=font_aw, bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=485, y = 20)

        lbl_buscar = tk.Label(self, text='Buscar: ', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_buscar.place(y=55, x=80)

        self.entry_buscar = ttk.Entry(self, width=50, font='roboto 12', background=color.FONDO_SEGUNDARIO)
        self.entry_buscar.place(y=80, x=80, height=40)
        self.entry_buscar.bind("<KeyRelease>", self.detectar_eliminacion)

        self.boton_buscar= tk.Button(self,text='Buscar \uf002', width=12, height=1 ,font=font_awesome ,bg=color.BOTON_PRODUCTOS, bd=0,
                                     command=self.buscar_producto)
        self.boton_buscar.place(x=720, y=80, height=40)

        self.boton_buscar_por = ttk.Combobox(self, values=('Buscar por: ID', 'Buscar por: desc') , width=24, height=1, font=font_awesome)
        self.boton_buscar_por.place(x=855, y=80, height=40)
        self.boton_buscar_por.current(0)

        self.create_scrollable_list()
       
    def create_scrollable_list(self):
        container = tk.Frame(self, bd=0.5)
        container.place(x=20, y=140, height=450, width=1080)

        header_frame = tk.Frame(container, bg=color.BOTON_PRODUCTOS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Imagen", width=14, height=2 ,anchor='w', bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Id", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Descripcion", width=20, height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Precio", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Cantidad", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Categoria", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Estado", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Opciones", width=15,height=2 ,anchor='w',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        
        self.canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        window_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')


        self.populate_list(self.productos.cargar_datos_consulta())
    
    def populate_list(self, datos):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=15)
        
        data = datos

        si = 0
        
        for item in data:            
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0
            estado = 'green' if item['estado'] else 'red'

            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill='x', pady=3)
            
            img_label = tk.Label(row_frame)
            img_label.pack(side='left', padx=5)
            
            try:
                image = leer_imagen(item['imagen'], (100,100))
            except Exception as e:
                image = leer_imagen('/imagenes/sinfoto.jpg', (100, 100))

            img_label.config(image=image)
            img_label.image = image
            
            tk.Label(row_frame, text=item['id'], width=15, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['desc']}", width=20, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['precio']}", width=15, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['cantidad']}", width=15, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['categoria']}", width=15, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['estado']}", width=15, anchor='center', bg=c, fg=estado).pack(side='left', padx=5)
        
            tk.Button(row_frame,text="\uf044", font=font_awesome, width=3, bg=color.BOTON_PRODUCTOS, bd = 0,
                      command=lambda i=item: self.edit_item(i)).pack(side='left', padx=5)
            
            tk.Button(row_frame, text="\uf1f8",font=font_awesome, width=3, bg=color.BOTON_PRODUCTOS, bd = 0,
                      command=lambda i=item, f=row_frame: self.delete_item(i, f)).pack(side='left', padx=5)
            
            tk.Button(row_frame, text="\uf2f1",font=font_awesome, width=3, bg=color.BOTON_ACCION, bd = 0,
                      command=lambda i =item : self.reponer_item(i)).pack(side='left', padx=5)
    
    def buscar_producto(self):
        if len(self.entry_buscar.get()) == 0:
            messagebox.showerror('Error', 'Campo de busqueda vacio')
            return
        
        formato = self.boton_buscar_por.get()

        if len(formato) == 0:
             messagebox.showerror('Error', 'Elija un metodo de busqueda')
             return
        
        if formato == 'Buscar por: ID':
            busqueda = self.productos.buscar_producto_id(self.entry_buscar.get())
            if busqueda == False:
                messagebox.showerror('Error', 'Datos incorrectos')
                return
            self.update_lista_busqueda(busqueda)

        elif formato == 'Buscar por: desc':
            busqueda = self.productos.buscar_producto_desc(self.entry_buscar.get())
            self.update_lista_busqueda(busqueda)

    def detectar_eliminacion(self,event):
        texto_actual = self.entry_buscar.get()
        
        if len(texto_actual) < len(self.ultimo_texto):
            if len(texto_actual) == 0 :
                self.update_lista_busqueda(self.productos.cargar_datos_consulta())
            elif self.boton_buscar_por.get() == 'Buscar por: desc':
                self.buscar_producto()
        else:
            if self.boton_buscar_por.get() == 'Buscar por: desc' and len(texto_actual) != 0:
                self.buscar_producto()

        self.ultimo_texto = texto_actual

    def edit_item(self, item):
        EditarProductoTop(self, item, self.update_lista)
    
    def reponer_item(self, item):
        ReponerProductoTop(self, item, self.update_lista)

    def delete_item(self, item, frame):
        delete = EliminarProducto()
        if messagebox.askyesno(title='Eliminar producto', message='¿Quieres eliminar el producto?'):
            if delete.delete_producto(item['id']):
                messagebox.showinfo(title='Mensaje', message='Se elimino el producto correctamente')
                frame.destroy()
            else:
                messagebox.showerror(title='Error', message='No se pudo borrar el producto')

    def update_lista(self):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        if len(self.entry_buscar.get()) != 0:
            self.buscar_producto()
        else:
             self.populate_list(self.productos.cargar_datos_consulta())

    def update_lista_busqueda(self, data):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.populate_list(data)            