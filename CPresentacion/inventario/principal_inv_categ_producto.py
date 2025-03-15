import tkinter as tk
import config as color

from tkinter import messagebox, font, ttk

from CPresentacion.inventario.principal_inv_editar import EditarProductoTop
from CPresentacion.inventario.principal_inv_reponer import ReponerProductoTop

from BDominio.productos.cargar_producto import CargarProductos
from BDominio.productos.eliminar_producto import EliminarProducto

from util.util_imagenes import leer_imagen

class CategoriaProductoTop(tk.Toplevel):
    def __init__(self, master, item):
        super().__init__(master)
        self.geometry('1000x600+190+40')
        self.title("Productos por categoria")
        self.resizable(0, 0)
        self.config(bg=color.FONDO_SEGUNDARIO)
        self.grab_set()

        self.categoria = item
        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)

        lbl_inventario = tk.Label(self, text='Productos/categoria', bg='white').pack(side=tk.TOP, anchor=tk.W)
        lbl = tk.Label(self, text=f"{self.categoria['descripcion']}", font='Lato 15', bg=color.FONDO_SEGUNDARIO)
        lbl.pack(pady=10)
        self.create_scrollable_list()
       
    def create_scrollable_list(self):
        container = tk.Frame(self, bd=0.5)
        container.pack(pady=30, padx=20, ipadx=110, ipady=100)
        header_frame = tk.Frame(container, bg=color.BOTON_PRODUCTOS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Imagen", width=14, height=2 ,anchor='w', bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Id", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Descripcion", width=20, height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Precio", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Cantidad", width=15,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
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
        #Datos de productos
        productos = CargarProductos()
        data = productos.productos_categoria(self.categoria['id'])

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
        if messagebox.askokcancel(title='Eliminar producto', message='¿Quieres eliminar el producto?'):
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