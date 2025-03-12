import tkinter as tk
import config as color

from BDominio.productos.cargar_producto import CargarProductos  #cargar datos de productos
from tkinter import ttk, messagebox, font, filedialog
from util.util_imagenes import leer_imagen
from BDominio.productos.eliminar_producto import EliminarProducto #eliminar producto

from CPresentacion.inventario.principal_inv_editar import EditarProductoTop #editar producto
from CPresentacion.inventario.principal_inv_categ_producto import CategoriaProductoTop

from BDominio.productos.categorias_datos import DatosCategoria
from BDominio.productos.eliminar_categoria import EliminarCategoria
from BDominio.productos.registrar_categoria import RegistrarCategoria
from BDominio.productos.editar_categoria import EditarCategoria

from util.util_imagenes import leer_imagen
from util.util_ventana import centrar_ventana

class InventarioCatalogo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)
        self.productos = CargarProductos()

        self.imagen_registro = ''
        self.imagen_edit = 'imagenes/sinfoto.jpg'

        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)
        font_aw= font.Font(family="Font Awesome" ,size=15)

        lbl_inventario = tk.Label(self, text='Inventario/consulta', bg='white').place(x=5, y=5)

        lbl = tk.Label(self, text="Categorias de productos \uf00b", font=font_aw, bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=485, y = 20)

        self.boton_nuevo = tk.Button(self,text='Nueva \uf0fe', width=12, height=1 ,font=font_awesome ,bg=color.BOTON_PRODUCTOS, bd=0,
                                     command=self.registrar_categoria)
        self.boton_nuevo.place(x=800, y=60, height=40)

        self.create_scrollable_list_categoria()
       
    def create_scrollable_list_categoria(self):
        container = tk.Frame(self, bd=0.5)
        container.place(x=150, y=120, height=450, width=800)

        # Crear encabezados
        header_frame = tk.Frame(container, bg=color.BOTON_PRODUCTOS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Imagen", width=14, height=2 ,anchor='w', bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Id", width=20,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Descripcion", width=20, height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Productos", width=20,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Opciones", width=20,height=2 ,anchor='center',  bg=color.BOTON_PRODUCTOS, font='roboto 9 ').pack(side='left', padx=5)
        
        self.canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        window_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.listar_categoria()
    
    def listar_categoria(self):
        font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=15)
        datos_categorias =  DatosCategoria()
        categorias = datos_categorias.datos_completos_categoria()
        si = 0

        for item in categorias:
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0

            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill=tk.X, pady=3)

            img_label = tk.Label(row_frame)
            img_label.pack(side='left', padx=5)
            
            try:
                image = leer_imagen(item['imagen'], (100,100))
                self.imagen_registro = item['imagen']
            except Exception as e:
                image = leer_imagen('imagenes/sinfoto.jpg', (100, 100))
                self.imagen_registro = 'imagenes/sinfoto.jpg'
            
            if image:
                img_label.config(image=image)
                img_label.image = image
            
            tk.Label(row_frame, text=item['id'], width=20, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=item['descripcion'], width=20, anchor='center', bg=c).pack(side='left', padx=5)

            tk.Button(row_frame, text=self.productos.producto_por_categoria(item['id']) , width=20, anchor='center',bg=color.BOTON_PRODUCTOS, bd=0,
                      command= lambda e = item : self.invetario_producto(e)).pack(side='left', padx=5)

            tk.Button(row_frame,text="\uf044", font=font_awesome, width=5, bg=color.BOTON_PRODUCTOS, bd = 0,
                      command=lambda i=item: self.editar_categoria(i)).pack(side='left', padx=10)
            tk.Button(row_frame, text="\uf1f8",font=font_awesome, width=5, bg=color.BOTON_PRODUCTOS, bd = 0,
                      command=lambda i=item, f=row_frame: self.delete_categoria(i, f)).pack(side='left', padx=10)
    

    def delete_categoria(self, item, frame):
        if messagebox.askokcancel('Mensaje', '¿Eliminar producto? \n si elimina la categoria todos los productos de esta seran eliminados') :
            eliminar = EliminarCategoria()
            if eliminar.eliminar_categoria(item['id']):
                messagebox.showinfo('Mensaje', 'Producto eliminado correctamente')
                frame.destroy()
            else:
                messagebox.showinfo('Mensaje', 'No se pudo eliminar la categoria')

    def registrar_categoria(self):
         self.registrar = tk.Toplevel(self)

         self.registrar.title('Editar Producto')
         self.registrar.geometry((centrar_ventana(self.registrar, 450, 600)))
         self.registrar.resizable(0, 0)
         self.registrar.grab_set()
         self.registrar.config(bg=color.FONDO_SEGUNDARIO)


         font_awesome = font.Font(family="Font Awesome " ,size=15)

         #=============================titulo======================================================
         lbl_titulo = tk.Label(self.registrar, text='Nueva Categoria \uf044', font=font_awesome, bg=color.FONDO_SEGUNDARIO)
         lbl_titulo.grid(row=0, column=0,  sticky=tk.NSEW, padx=10, pady=10)

        #=======================frame formulario================================================
         self.frame_formulario = tk.Frame(self.registrar, bg=color.FONDO_SEGUNDARIO)
         self.frame_formulario.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=10)

         #=======================Widgets=======================================================
         #imagen
         lbl_imagen = tk.Label(self.frame_formulario, text='Imagen', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
         lbl_imagen.grid(row=0, column=0, padx=15, pady=5)

         self.imagen = tk.Label(self.frame_formulario,  background=color.FONDO_PRINCIPAL)
         self.imagen.grid(row=0, column=1, padx=15, pady=5)

         try: 
            image = leer_imagen('imagenes/sinfoto.jpg', (120, 120))
         except Exception as e:
            print('error a cargar la imagen de prueba')

         if image:
                self.imagen.config(image=image)
                self.imagen.image = image

         
         self.button_imagen = tk.Button(self.frame_formulario, text='Cargar', font=('roboto', 12), bg=color.BOTON_PRODUCTOS,
                                    command=self.load_imagen)
         self.button_imagen.grid(row=1, column=1, ipadx=6, ipady=2)

         #descripcion
         lbl_descripcion = tk.Label(self.frame_formulario, text='Descripcion', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_descripcion.grid(row=3,  column=0, padx=20, pady=20)
         self.entry_descripcion = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
         self.entry_descripcion.grid(row=3, column=1, padx=20, pady=20, ipady=8)
            
         #botones
         self.boton_guardar = tk.Button(self.frame_formulario, text='Guardar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                       command=self.guardar_categoria)
         self.boton_guardar.grid(row=4, column=0, ipadx=30,pady=10 ,ipady=6, sticky=tk.E)

         self.boton_cancelar = tk.Button(self.frame_formulario, text='Cancelar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                        command=self.registrar.destroy)
         self.boton_cancelar.grid(row=4, column=1, ipadx=30 , pady=10, ipady=6, sticky=tk.E)

    def guardar_categoria(self):
        imagen = self.imagen_registro
        descripcion = self.entry_descripcion.get()

        if len(descripcion) == 0:
            messagebox.showerror('Error', 'Campo de texto vacio')
            return
        
        if messagebox.askokcancel('Mensaje', '¿Registrar categoria?'):
            registrar = RegistrarCategoria()
            confirmacion = registrar.registrar_categoria(descripcion, imagen)
            if confirmacion:
                messagebox.showinfo('Mensaje', 'Categoria registrada correctamente')
                self.registrar.destroy()
                self.update_categoria()
            else:
                messagebox.showerror('Error', 'No se pudo registrar la categoria')

    def editar_categoria(self, item):
         self.editar = tk.Toplevel(self)

         self.editar.title('Editar Producto')
         self.editar.geometry((centrar_ventana(self.editar, 450, 600)))
         self.editar.resizable(0, 0)
         self.editar.grab_set()
         self.editar.config(bg=color.FONDO_SEGUNDARIO)


         font_awesome = font.Font(family="Font Awesome " ,size=15)

         #=============================titulo======================================================
         lbl= tk.Label(self.editar, text='Editar Categoria \uf044', font=font_awesome, bg=color.FONDO_SEGUNDARIO)
         lbl.grid(row=0, column=0,  sticky=tk.NSEW, padx=10, pady=10)

        #=======================frame formulario================================================
         self.frame_for = tk.Frame(self.editar, bg=color.FONDO_SEGUNDARIO)
         self.frame_for.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=10)

         #=======================Widgets=======================================================
         #imagen
         lbl_imag = tk.Label(self.frame_for, text='Imagen', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
         lbl_imag.grid(row=0, column=0, padx=15, pady=5)

         self.imag = tk.Label(self.frame_for,  background=color.FONDO_PRINCIPAL)
         self.imag.grid(row=0, column=1, padx=15, pady=5)

         try: 
            img = leer_imagen(item['imagen'], (120, 120))
            self.imag.config(image=img)
            self.imag.image = img
         except Exception as e:
            print('error a cargar la imagen de prueba')
         
         self.button_imag = tk.Button(self.frame_for, text='Cargar', font=('roboto', 12), bg=color.BOTON_PRODUCTOS,
                                       command= lambda e = True: self.load_imagen(e))
         self.button_imag.grid(row=1, column=1, ipadx=6, ipady=2)

         #id
         lb_id = tk.Label(self.frame_for, text='Id_categoria', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lb_id.grid(row=2,  column=0, padx=20, pady=20)
         self.entryid = ttk.Entry(self.frame_for,width=20,  font=('roboto', 12))
         self.entryid.grid(row=2, column=1, padx=20, pady=20, ipady=8)
         self.entryid.insert(0, item['id'])
         self.entryid.config(state=tk.DISABLED)

         #descripcion
         lb_descripcion = tk.Label(self.frame_for, text='Descripcion', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lb_descripcion.grid(row=3,  column=0, padx=20, pady=20)
         self.entrydescripcion = ttk.Entry(self.frame_for,width=20,  font=('roboto', 12))
         self.entrydescripcion.grid(row=3, column=1, padx=20, pady=20, ipady=8)
         self.entrydescripcion.insert(0, item['descripcion'])
            
         #botones
         self.botonguardar = tk.Button(self.frame_for, text='Guardar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                       command=self.guardar_edit)
         self.botonguardar.grid(row=4, column=0, ipadx=30,pady=10 ,ipady=6, sticky=tk.E)

         self.botoncancelar = tk.Button(self.frame_for, text='Cancelar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                        command=self.editar.destroy)
         self.botoncancelar.grid(row=4, column=1, ipadx=30 , pady=10, ipady=6, sticky=tk.E)

    def guardar_edit(self):
        descripcion = self.entrydescripcion.get()
        self.entryid.config(state=tk.NORMAL)
        id = self.entryid.get()
        self.entryid.config(state=tk.DISABLED)
        imagen = self.imagen_edit

        if len(descripcion) == 0:
            messagebox.showerror('Error', 'Campos vacios', parent = self.editar)
            return

        if messagebox.askokcancel('Mensaje', '¿Editar categoria?', parent = self.editar):
            actualizar = EditarCategoria()
            if actualizar.actualizar_categoria(id, descripcion, imagen):
                messagebox.showinfo('Mensaje', 'Categoria actualizada', parent = self.editar)
                self.editar.destroy()
                self.update_categoria()
            else:
                messagebox.showerror('Error', 'No se pudo actualizar', parent = self.editar) 

    def load_imagen(self, edit = False):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                imagen = leer_imagen(file_path, (120, 120))
            except:
                print('No se pudo cargar la imagen')
                return
            if edit:
                self.imag.config(image=imagen)
                self.imag.image = imagen
                self.imagen_edit = file_path
            else :
                self.imagen.config(image=imagen)
                self.imagen.image = imagen
                self.imagen_registro = file_path

    def update_categoria(self):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.listar_categoria()

    def invetario_producto(self, item):
        CategoriaProductoTop(self, item)
