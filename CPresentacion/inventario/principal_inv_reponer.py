import tkinter as tk
import config as color

from util.util_ventana import centrar_ventana
from tkinter import font, messagebox, ttk, filedialog
from util.util_imagenes import leer_imagen
from BDominio.productos.categorias_datos import DatosCategoria
from BDominio.productos.editar_producto import EditarProducto


class ReponerProductoTop(tk.Toplevel):
    def __init__(self, master, producto, update_lista):
        super().__init__(master)
        self.title('R Producto')
        self.geometry((centrar_ventana(self, 450, 600)))
        self.resizable(0, 0)
        self.grab_set()
        self.config(bg=color.FONDO_SEGUNDARIO)

        self.producto = producto
        self.actualizar_lista = update_lista
        self.create_widgets()

    def create_widgets(self):
        font_awesome = font.Font(family="Font Awesome " ,size=15)

        #=============================titulo======================================================
        lbl_titulo = tk.Label(self, text='Reponer Producto \uf2f1', font=font_awesome, bg=color.FONDO_SEGUNDARIO)
        lbl_titulo.grid(row=0, column=0,  sticky=tk.NSEW, padx=10, pady=10)

        #=======================frame formulario================================================
        self.frame_formulario = tk.Frame(self, bg=color.FONDO_SEGUNDARIO)
        self.frame_formulario.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=10)

        #=======================Widgets=======================================================
        #imagen
        lbl_imagen = tk.Label(self.frame_formulario, text='Imagen', font=('roboto', 12), background=color.FONDO_SEGUNDARIO)
        lbl_imagen.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.imagen = tk.Label(self.frame_formulario)
        self.imagen.grid(row=0, column=1, padx=15, pady=5)

        img = leer_imagen(self.producto['imagen'], (120, 120))
        if img:
                self.imagen.config(image=img)
                self.imagen.image = img
        
        #descripcion
        lbl_descripcion = tk.Label(self.frame_formulario, text='Descripcion', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_descripcion.grid(row=3,  column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_descripcion = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_descripcion.grid(row=3, column=1, padx=10, pady=5, ipady=5)
        self.entry_descripcion.insert(0, self.producto['desc'])
        self.entry_descripcion.config(state=tk.DISABLED)

        #Cantidad
        lbl_cantidad = tk.Label(self.frame_formulario, text='Cantidad', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_cantidad.grid(row=5,  column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_cantidad = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_cantidad.grid(row=5, column=1, padx=10, pady=5, ipady=5)
        self.entry_cantidad.insert(0, self.producto['cantidad'])
        self.entry_cantidad.config(state=tk.DISABLED)

        lbl_info = tk.Label(self.frame_formulario, text='Cantidad a reponer: ', font='roboto 11', bg=color.FONDO_SEGUNDARIO)
        lbl_info.grid(row=6, column=0, sticky=tk.W, pady=10, padx=10)

        self.entry_cantidad_reponer = ttk.Entry(self.frame_formulario,width=20,  font=('roboto', 12))
        self.entry_cantidad_reponer.grid(row=7, column=0, padx=10, pady=5, ipady=5, sticky=tk.E)

        #botones
        self.boton_guardar = tk.Button(self.frame_formulario, text='Reponer', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                       command=self.guardar_cambios)
        self.boton_guardar.grid(row=8, column=0, ipadx=15, padx=10 ,pady=10, ipady=5, sticky=tk.E)

        self.boton_cancelar = tk.Button(self.frame_formulario, text='Cancelar', font='roboto 12', bg=color.BOTON_PRODUCTOS, bd=0,
                                        command=self.destroy)
        self.boton_cancelar.grid(row=8, column=1, ipadx=15 , pady=10, ipady=5, sticky=tk.W)

    def guardar_cambios(self):      
         if len(self.entry_cantidad_reponer.get()) == 0:
            messagebox.showerror('Error', 'Campo reponer vacio')
            return 0
         
         cantidad = self.entry_cantidad_reponer.get()

         editar = EditarProducto()

         if messagebox.askretrycancel('Reponer producto', '¿Quieres guardar los cambios?'): 
            if editar.reponer_producto(self.producto['id'], cantidad):
                 messagebox.showinfo('Mensaje', 'Cambios guardados correctamente')
                 self.destroy()
                 self.actualizar_lista()
            else:
                 messagebox.showwarning('Error', 'Datos incopatibles')
