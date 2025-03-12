import tkinter as tk
import config as color

from util.util_ventana import centrar_ventana
from tkinter import font, messagebox, ttk, filedialog
from util.util_imagenes import leer_imagen
from BDominio.productos.categorias_datos import DatosCategoria
from BDominio.productos.editar_producto import EditarProducto

class EditarProductoTop(tk.Toplevel):
    def __init__(self, master, producto, update_lista):
        super().__init__(master)
        self.title('Editar Producto')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=color.FONDO_SEGUNDARIO)

        self.categoria = DatosCategoria()
        self.categorias = self.categoria.Datos_categoria()
        self.producto = producto
        self.actualizar_lista = update_lista
        self.create_widgets()

    def create_widgets(self):
        font_awesome = font.Font(family="Font Awesome " ,size=15)

        #=============================titulo======================================================
        lbl_titulo = tk.Label(self, text='Editar Producto \uf044', font=font_awesome, bg=color.FONDO_SEGUNDARIO)
        lbl_titulo.grid(row=0, column=0,  sticky=tk.NSEW, padx=10, pady=10)

        #=======================frame formulario================================================
        self.frame_formulario = tk.Frame(self, bg=color.FONDO_SEGUNDARIO)
        self.frame_formulario.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=10)

        #=======================Widgets=======================================================
        #imagen
        lbl_imagen = tk.Label(self.frame_formulario, text='Imagen', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
        lbl_imagen.grid(row=0, column=0, padx=15, pady=5)

        self.imagen = tk.Label(self.frame_formulario)
        self.imagen.grid(row=0, column=1, padx=15, pady=5)

        img = leer_imagen(self.producto['imagen'], (120, 120))
        if img:
                self.imagen.config(image=img)
                self.imagen.image = img

        self.button_imagen = tk.Button(self.frame_formulario, text='Cargar', font=('roboto', 12), bg=color.BOTON_PRODUCTOS,
                                       command=self.cargar_imagen)
        self.button_imagen.grid(row=1, column=1, ipadx=5)


        #id_producto
        lbl_id_producto = tk.Label(self.frame_formulario, text='Id_producto', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_id_producto.grid(row=2,  column=0, padx=15, pady=5)
        self.entry_id = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_id.grid(row=2, column=1, padx=15, pady=5, ipady=5)
        self.entry_id.insert(0,self.producto['id'])
        self.entry_id.config(state=tk.DISABLED)
        
        #descripcion
        lbl_descripcion = tk.Label(self.frame_formulario, text='Descripcion', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_descripcion.grid(row=3,  column=0, padx=15, pady=5)
        self.entry_descripcion = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_descripcion.grid(row=3, column=1, padx=15, pady=5, ipady=5)
        self.entry_descripcion.insert(0, self.producto['desc'])

        #Precio
        lbl_precio = tk.Label(self.frame_formulario, text='Precio', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_precio.grid(row=4,  column=0, padx=15, pady=5)
        self.entry_precio = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_precio.grid(row=4, column=1, padx=15, pady=15, ipady=5)
        self.entry_precio.insert(0, self.producto['precio'])

        #Cantidad
        lbl_cantidad = tk.Label(self.frame_formulario, text='Cantidad', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_cantidad.grid(row=5,  column=0, padx=15, pady=5)
        self.entry_cantidad = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_cantidad.grid(row=5, column=1, padx=15, pady=5, ipady=5)
        self.entry_cantidad.insert(0, self.producto['cantidad'])
        self.entry_cantidad.config(state=tk.DISABLED)

        #categorias

        lbl_categoria= tk.Label(self.frame_formulario, text='Categoria', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
        lbl_categoria.grid(row=6, column=0, padx=15, pady=5)
        self.Combobox_categoria = ttk.Combobox(self.frame_formulario, values=self.categorias, width=18,  font=('roboto', 12))
        self.Combobox_categoria.grid(row=6, column=1, padx=15, pady=5, ipady=5)
        self.Combobox_categoria.set(f'{self.producto['categoria']}')        

        #estado
        lbl_estado = tk.Label(self.frame_formulario, text='estado', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
        lbl_estado.grid(row=7, column=0, padx=15, pady=5)
        self.entry_estado = ttk.Combobox(self.frame_formulario, values=('True', 'False'), width=18,  font=('roboto', 12))
        self.entry_estado.grid(row=7, column=1, padx=15, pady=5, ipady=5)
        self.entry_estado.set(f'{self.producto['estado']}')

        #Fecha
        if self.producto['fecha'] != None:
            lbl_fecha = tk.Label(self.frame_formulario, text='Fecha_ven', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
            lbl_fecha.grid(row=8,  column=0, padx=15, pady=5)
            self.entry_fecha = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
            self.entry_fecha.grid(row=8, column=1, padx=15, pady=5, ipady=5)
            self.entry_fecha.insert(0, self.producto['fecha'])
            
        #botones
        self.boton_guardar = tk.Button(self.frame_formulario, text='Guardar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                       command=self.guardar_cambios)
        self.boton_guardar.grid(row=9, column=0, ipadx=15, padx=10 ,pady=10, ipady=5, sticky=tk.E)

        self.boton_cancelar = tk.Button(self.frame_formulario, text='Cancelar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                        command=self.destroy)
        self.boton_cancelar.grid(row=9, column=1, ipadx=15 , pady=10, ipady=5, sticky=tk.E)

    def cargar_imagen(self):
        file_path = filedialog.askopenfilename() #abre cuadro de dialogo
        if file_path:
             img = leer_imagen(file_path, (120, 120)) #Abre la imagen
             # extrae el nombre completo
             self.producto['imagen'] = file_path
             self.imagen.config(image=img)
             self.imagen.image = img

    def guardar_cambios(self):
         imagen = self.producto['imagen']
         id = self.entry_id.get()
         descripcrion = self.entry_descripcion.get()
         precio = self.entry_precio.get()
         self.entry_cantidad.config(state=tk.NORMAL)
         cantidad = self.entry_cantidad.get()
         self.entry_cantidad.config(state=tk.DISABLED)
         categoria = self.categoria.id_categoria(self.Combobox_categoria.get())
         estado = self.entry_estado.get()
         fecha = '0'

         if self.producto['fecha'] != None:
            fecha = self.entry_fecha.get()
        

         if not self.campos_vacios(descripcrion, precio, cantidad, fecha):
            messagebox.showerror(title='Mensaje', message='Campos vacios', parent = self)
            return
         
         editar = EditarProducto()

         if messagebox.askretrycancel('Editar producto', '¿Quieres guardar los cambios?', parent = self): 
            if editar.editar_producto(id, descripcrion, precio, cantidad, fecha, categoria, imagen, estado):
                 messagebox.showinfo('Mensaje', 'Cambios guardados correctamente', parent = self)
                 self.destroy()
                 self.actualizar_lista()
            else:
                 messagebox.showwarning('Error', 'A ocurrido un error inesperado', parent = self)
                 
    def campos_vacios(self, desc, pre, cant, fecha):
         if len(desc) != 0 and len(pre) != 0 and len(cant) != 0 and len(fecha) != 0:
              return True
         return False
             





        







