import tkinter as tk
import config as color
import os
import webbrowser

from tkinter import ttk, messagebox, font

from BDominio.ventas.cargar_datos_venta import DatosVenta
from BDominio.ventas.eliminar_venta import EliminarVenta

class VentasConsulta(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)

        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)

        lbl_inventario = tk.Label(self, text='Venta/Lista de ventas', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Registro de ventas", font='Lato 15', bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=485, y = 20)

        self.create_scrollable_list()
       
    def create_scrollable_list(self):
        container = tk.Frame(self, bd=0.5)
        container.place(x=20, y=120, height=500, width=1080)

        header_frame = tk.Frame(container, bg=color.BOTON_VENTAS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Id_venta", width=23, height=2 ,anchor='center', bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Precio Total", width=23,height=2 ,anchor='center',  bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Fecha", width=23,height=2 ,anchor='center',  bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Hora", width=23,height=2 ,anchor='center',  bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Usuario", width=23, height=2, anchor='center',  bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Opciones", width=35,height=2 ,anchor='w',  bg=color.BOTON_VENTAS, font='roboto 9 ').pack(side='left', padx=5)
        
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
        ventas = DatosVenta()
        data = ventas.consultar_ventas()

        si = 0
        
        for item in data:            
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0

            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill='x', pady=3)
            
            tk.Label(row_frame, text=item['id'], width=23, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"Bs.{item['precio_total']}", width=23, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['fecha']}", width=23, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['hora']}", width=23, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{item['dni_usuario']}", width=23, anchor='center', bg=c).pack(side='left', padx=5)
           
            tk.Button(row_frame,text="\uf571", font=font_awesome, width=4, bg=color.BOTON_VENTAS, bd = 0,
                      command=lambda i=item: self.ver_item(i)).pack(side='left', padx=7)
            
            tk.Button(row_frame, text="\uf1f8",font=font_awesome, width=4, bg=color.BOTON_VENTAS, bd = 0,
                      command=lambda i=item, f=row_frame: self.delete_item(i, f)).pack(side='left', padx=7)
                 
    def ver_item(self, item):
        # Definir la carpeta donde están las facturas
        carpeta_facturas = r"C:\Users\pedro\OneDrive\Documentos\facturas"

        # Construir la ruta del archivo PDF
        nombre_archivo = f"factura_{item['id']}.pdf"
        ruta_factura = os.path.join(carpeta_facturas, nombre_archivo)

        # Verificar si la factura existe y abrirla
        if os.path.exists(ruta_factura):
            print(f"Abriendo factura: {ruta_factura}")
            webbrowser.open(ruta_factura)
        else:
            messagebox.showerror('Error',f"Factura {item['id']} no encontrada en {carpeta_facturas}")

    def delete_item(self, item, frame):
        delete = EliminarVenta()
        if messagebox.askokcancel(title='Eliminar venta', message='¿Quieres eliminar la venta?'):
            if delete.eliminar_venta(item['id']):
                messagebox.showinfo(title='Mensaje', message='Se elimino el producto correctamente')
                frame.destroy()
            else:
                messagebox.showerror(title='Error', message='No se pudo borrar el producto')

    def update_lista(self):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.populate_list() 