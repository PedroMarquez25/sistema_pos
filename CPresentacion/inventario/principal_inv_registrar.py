import tkinter as tk
import config as color

from tkinter import font, ttk, messagebox, filedialog
from BDominio.productos.categorias_datos import DatosCategoria
from BDominio.productos.registrar_producto import RegistrarProducto
from util.util_imagenes import leer_imagen

class InventarioRegistrar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)

        self.categoria = DatosCategoria()
        self.categorias = self.categoria.Datos_categoria()
        self.crear_widgets()

    def crear_widgets(self):
        font_awesome = font.Font(family="Font Awesome" ,size=15)
        pax, pay, ix, iy = 35, 10, 70, 8

        lbl_inventario = tk.Label(self, text='Inventario/registro', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Registrar productos \uf0fe", font=font_awesome, bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=450, y = 20)

        #=====================frame del formulario===========================================
        self.formulario = tk.Frame(self, bg=color.FONDO_SEGUNDARIO, bd=0.5, relief='groove' )
        self.formulario.place(y=80, x=160, height=500, width=790)

        #=============================widgets================================================
        lbl_informacion_general = tk.Label(self.formulario, text='Informacion general', font='roboto 12 bold', bg=color.FONDO_SEGUNDARIO)
        lbl_informacion_general.grid(row=0,column=0,pady=10 ,sticky=tk.W)

        lbl_ingrese_datos = tk.Label(self.formulario, text='Ingrese los datos del producto', font='roboto 11', bg=color.FONDO_SEGUNDARIO)
        lbl_ingrese_datos.grid(row=1,column=0, padx=30,pady=pay ,sticky=tk.W)

        #descripcion
        lbl_descripcion = tk.Label(self.formulario, text='Descripcion', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_descripcion.grid(row=2,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_descripcion = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_descripcion.grid(row=3, column=0, padx=pax , pady=pay, ipadx=ix, ipady=iy)

        #Categorias
        lbl_categoria = tk.Label(self.formulario, text='Categoria', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_categoria.grid(row=2,column=1, padx=pax, pady=pay, sticky=tk.W)
        self.entry_categoria = ttk.Combobox(self.formulario, font='roboto 12', values=self.categorias)
        self.entry_categoria.grid(row=3, column=1, padx=pax, pady=pay, ipadx=65, ipady=iy)

        #Cantidad
        lbl_cantidad = tk.Label(self.formulario, text='Cantidad', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_cantidad.grid(row=4,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_cantidad = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_cantidad.grid(row=5, column=0, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #precio
        lbl_precio = tk.Label(self.formulario, text='Precio', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_precio.grid(row=4,column=1, padx=pax, pady=pay, sticky=tk.W)
        self.entry_precio = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_precio.grid(row=5, column=1, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #fecha_vencimieto
        lbl_fecha_vencimieto = tk.Label(self.formulario, text='Fecha vencimieto', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_fecha_vencimieto.grid(row=6,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_fecha_vencimieto = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_fecha_vencimieto.grid(row=7, column=0, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #cargar imagen
        lbl_Cargar_imagen = tk.Label(self.formulario, text='Cargar imagen', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_Cargar_imagen.grid(row=6,column=1, padx=pax, pady=pay, sticky=tk.W)
        self.Cargar_imagen = ttk.Entry(self.formulario, font='roboto 12')
        self.Cargar_imagen.grid(row=7, column=1, padx=pax, pady=pay, ipadx=20, ipady=iy, sticky=tk.W)
        self.Cargar_imagen.config(state=tk.DISABLED)

        #botones
        self.boton_cargar = tk.Button(self.formulario, text='Cargar', font='roboto 12',bg=color.BOTON_PRODUCTOS, 
                                      command=self.load_imagen)
        self.boton_cargar.grid(row=7, column=1,padx=pax, pady=pay, ipadx=10, ipady=5, sticky=tk.E)

        self.boton_guardar = tk.Button(self.formulario, text='Guardar \uf0fe',font=font_awesome ,bg=color.BOTON_PRODUCTOS, width=20, height=1, bd=0,
                                       command=self.registrar_producto)
        self.boton_guardar.grid(row=9, column=0, padx=pax, pady=20, ipady=1, sticky=tk.E)

        self.boton_limpiar = tk.Button(self.formulario, text='Limpiar campos',font=font_awesome  ,bg=color.BOTON_PRODUCTOS, width=20, height=1, bd=0,
                                       command=self.limpiar_campos)
        self.boton_limpiar.grid(row=9, column=1, padx=pax, pady=20, ipady=1 ,sticky=tk.W)

    def registrar_producto(self):
        descripcion = self.entry_descripcion.get()
        categoria = self.entry_categoria.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()
        fecha_ven = self.entry_fecha_vencimieto.get()
        imagen = self.Cargar_imagen.get()

        if len(fecha_ven) == 0:
            fecha_ven = '0'

        if len(imagen) == 0:
            imagen = 'imagenes/sinfoto.jpg'
            
        
        if len(descripcion) == 0 or len(categoria) == 0 or len(cantidad) == 0 or len(precio) == 0:
            messagebox.showerror('Mensaje', 'Complete todos los campos')
            return
        
        if messagebox.askokcancel('Registrar_producto', '¿Guardar producto?'):
            registrar = RegistrarProducto()
            confirmacion = registrar.regitrar(descripcion, precio, cantidad, fecha_ven, categoria, imagen)
            if confirmacion == 1:
                messagebox.showwarning('Error', 'Datos incorrectos')
            elif confirmacion == 2:
                messagebox.showwarning('Error', 'Error con la base de datos')
            elif confirmacion == 3:
                messagebox.showinfo('Mensaje', 'Producto registrado correctamente')
                self.limpiar_campos()
    
    def load_imagen(self):
        file_path = filedialog.askopenfilename() #abre cuadro de dialogo
        if file_path:
             self.Cargar_imagen.config(state=tk.NORMAL)
             self.Cargar_imagen.insert(0,file_path)
             self.Cargar_imagen.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.entry_descripcion.delete(0, 'end')
        self.entry_categoria.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')
        self.entry_precio.delete(0, 'end')
        self.entry_fecha_vencimieto.delete(0, 'end')
        self.Cargar_imagen.config(state=tk.NORMAL)
        self.Cargar_imagen.delete(0, 'end')
        self.Cargar_imagen.config(state=tk.DISABLED)


        
        







