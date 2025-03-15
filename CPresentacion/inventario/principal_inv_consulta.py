import tkinter as tk
import config as color

from tkinter import ttk, messagebox, font

from CPresentacion.inventario.principal_inv_editar import EditarProductoTop
from CPresentacion.inventario.principal_inv_reponer import ReponerProductoTop

from BDominio.productos.eliminar_producto import EliminarProducto
from BDominio.productos.cargar_producto import CargarProductos

from util.util_imagenes import leer_imagen

class InventarioConsulta(tk.Frame):
    def __init__(self, parent, inventario_registrar):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)

        self.invetario_registrar = inventario_registrar

        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)

        lbl_inventario = tk.Label(self, text='Inventario/consulta', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Lista de productos", font='Lato 15', bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=485, y = 20)

        self.boton_nuevo = tk.Button(self,text='Nuevo \uf0fe', width=12, height=1 ,font=font_awesome ,bg=color.BOTON_PRODUCTOS, bd=0,
                                     command=self.invetario_registrar)
        self.boton_nuevo.place(x=975, y=60, height=40)

        self.boton_buscar = tk.Button(self, text='Buscar \uf002', width=12, height=1, font=font_awesome, bg=color.BOTON_PRODUCTOS, bd=0)
        self.boton_buscar.place(x=855, y=60, height=40)

        self.create_scrollable_list()
       
    def create_scrollable_list(self):
        container = tk.Frame(self, bd=0.5)
        container.place(x=20, y=120, height=500, width=1080)

        # Crear encabezados
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
        
        self.populate_list()
    
    def populate_list(self):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=15)
        productos = CargarProductos()
        data = productos.cargar_datos_consulta()

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
                image = leer_imagen('imagenes/sinfoto.jpg', (100, 100))

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
    
    def edit_item(self, item):
        EditarProductoTop(self, item, self.update_lista)

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
        self.populate_list()
    
    def reponer_item(self, item):
        ReponerProductoTop(self, item, self.update_lista)