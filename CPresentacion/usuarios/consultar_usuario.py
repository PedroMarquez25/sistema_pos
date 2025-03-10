import tkinter as tk
import config as color


from tkinter import ttk, messagebox, font
from util.util_imagenes import leer_imagen
from util.util_ventana import centrar_ventana

from BDominio.usuarios.cargar_usuarios import CargarUsuario
from BDominio.usuarios.validar_usuario import UsuarioValid
from BDominio.usuarios.editar_usuario import EditarUsuario


class UsuarioConsulta(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)

        self.usuarios = CargarUsuario()

        self.create_widget()
    
    def create_widget(self):   
        font_awesome = font.Font(family="Font Awesome" ,size=13)

        lbl_inventario = tk.Label(self, text='Usuario/consulta', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Lista de usuarios", font='Lato 15', bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=485, y = 20)

        self.boton_nuevo = tk.Button(self,text='Nuevo \uf0fe', width=12, height=1 ,font=font_awesome ,bg=color.BOTON_USUARIOS, bd=0,
                                     )
        self.boton_nuevo.place(x=975, y=60, height=40)

        self.create_scrollable_list()
       
    def create_scrollable_list(self):
        container = tk.Frame(self, bd=0.5)
        container.place(x=20, y=120, height=500, width=1080)

        # Crear encabezados
        header_frame = tk.Frame(container, bg=color.BOTON_USUARIOS)
        header_frame.pack(fill='x')
        
        tk.Label(header_frame, text="Dni", width=16, height=2 ,anchor='center', bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Nombre", width=16,height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="usuario", width=16, height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Clave", width=16,height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Rol", width=16,height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Acceso", width=16,height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Caja", width=15,height=2 ,anchor='center',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        tk.Label(header_frame, text="Opciones", width=15,height=2 ,anchor='w',  bg=color.BOTON_USUARIOS, font='roboto 9 ').pack(side='left', padx=5)
        
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
        #Datos de BOTON_USUARIOS
        data = self.usuarios.Cargar_datos_usuario()

        si = 0
        
        for usuario in data:            
            c = 'white' if si == 0 else "lightgray"
            si = 1 if si == 0 else 0


            row_frame = tk.Frame(self.scrollable_frame, bg=c)
            row_frame.pack(fill='x', pady=3)
                    
            tk.Label(row_frame, text=usuario['dni'], width=16, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['nombre']}", width=16, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['usuario']}", width=16, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['clave']}", width=16, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['rol']}", width=16, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['acceso']}", width=15, anchor='center', bg=c).pack(side='left', padx=5)
            tk.Label(row_frame, text=f"{usuario['n_caja']}", width=15, anchor='center', bg=c).pack(side='left', padx=5)
        
            tk.Button(row_frame,text="\uf044", font=font_awesome, width=3, bg=color.BOTON_USUARIOS, bd = 0,
                      command=lambda e = usuario : self.edit_usuario(e)).pack(side='left', padx=5)
                
            tk.Button(row_frame, text="\uf1f8",font=font_awesome, width=3, bg=color.BOTON_USUARIOS, bd = 0,
                      ).pack(side='left', padx=5)
            
            tk.Button(row_frame, text="\uf2f1",font=font_awesome, width=3, bg=color.BOTON_ACCION, bd = 0,
                      ).pack(side='left', padx=5)
    
    def edit_usuario(self, usuario):
         font_awesome = font.Font(family='font awesome', size=15)

         self.frame_edit_usario = tk.Toplevel(self)
         self.frame_edit_usario.title('Editar usuario')
         self.frame_edit_usario.geometry(centrar_ventana(self.frame_edit_usario, 450, 600))
         self.frame_edit_usario.resizable(0,0)
         self.frame_edit_usario.grab_set()
         self.frame_edit_usario.config(bg=color.FONDO_SEGUNDARIO)

         lbl_titulo = tk.Label(self.frame_edit_usario, text="Editar usuario \uf044", font=font_awesome, bg=color.FONDO_SEGUNDARIO)
         lbl_titulo.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=5)

            #===========================Formulario de registro============================================
         lblfrme_nuevo_usuario = tk.LabelFrame(self.frame_edit_usario, text='Datos personales' ,bg=color.FONDO_SEGUNDARIO, bd=0.5)
         lblfrme_nuevo_usuario.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=15)

         self.address_imagen = usuario['imagen']
         self.usuario_original = usuario['usuario']
         self.acceso_original = usuario['acceso']

         lbl_dni_usario = tk.Label(lblfrme_nuevo_usuario, text='DNI', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_dni_usario.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
         self.txt_dni_usario = ttk.Entry(lblfrme_nuevo_usuario, width=20,  font=('roboto', 12))
         self.txt_dni_usario.grid(row=0, column=1, padx=10, pady=10, ipady=5)
         self.txt_dni_usario.insert(0, usuario['dni'])
         self.txt_dni_usario.config(state=tk.DISABLED)
         
         lbl_nombre_usario = tk.Label(lblfrme_nuevo_usuario, text='Nombre', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_nombre_usario.grid(row=1, column=0, padx=10, pady=10,  sticky=tk.W)
         self.txt_nombre_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
         self.txt_nombre_usario.grid(row=1, column=1, padx=10, pady=10, ipady=5)
         self.txt_nombre_usario.insert(0, usuario['nombre'])

         lbl_usuario_usario = tk.Label(lblfrme_nuevo_usuario, text='Usuario', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_usuario_usario.grid(row=2, column=0, padx=10, pady=10,  sticky=tk.W)
         self.txt_usuario_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
         self.txt_usuario_usario.grid(row=2, column=1, padx=10, pady=10, ipady=5)
         self.txt_usuario_usario.insert(0, usuario['usuario'])

         lbl_clave_usario = tk.Label(lblfrme_nuevo_usuario, text='Contraseña', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_clave_usario.grid(row=3, column=0, padx=10, pady=10,  sticky=tk.W)
         self.txt_clave_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
         self.txt_clave_usario.grid(row=3, column=1, padx=10, pady=10, ipady=5)
         self.txt_clave_usario.insert(0, usuario['clave'])

         lbl_clave_usario2 = tk.Label(lblfrme_nuevo_usuario, text='Repetir contraseña', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_clave_usario2.grid(row=4, column=0, padx=10, pady=10,  sticky=tk.W)
         self.txt_clave_usario2 = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
         self.txt_clave_usario2.grid(row=4, column=1, padx=10, pady=10, ipady=5)
         self.txt_clave_usario2.insert(0, usuario['clave'])

         lbl_rol_usario = tk.Label(lblfrme_nuevo_usuario, text='Rol', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_rol_usario.grid(row=5, column=0, padx=10, pady=10,  sticky=tk.W)
         self.txt_rol_usario = ttk.Combobox(lblfrme_nuevo_usuario, values=('Cajero', 'Aministrador'), width=18,  font=('roboto', 12))
         self.txt_rol_usario.grid(row=5, column=1, padx=10, pady=10, ipady=5)
         self.txt_rol_usario.set(usuario['rol'])

         acceso = 'Permitido' if usuario['acceso'] > 0 else 'Denegado'
         lbl_acceso_usario = tk.Label(lblfrme_nuevo_usuario, text='Acceso', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_acceso_usario.grid(row=6, column=0, padx=10, pady=10,  sticky=tk.W)
         self.acceso_usario = ttk.Combobox(lblfrme_nuevo_usuario, values=('Permitido', 'Denegado'), width=18,  font=('roboto', 12))
         self.acceso_usario.grid(row=6, column=1, padx=10, pady=10, ipady=5)
         self.acceso_usario.set(acceso)
         self.acceso_usario.config(state=tk.DISABLED)

         lbl_caja_usario = tk.Label(lblfrme_nuevo_usuario, text='Caja', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
         lbl_caja_usario.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)
         self.caja_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
         self.caja_usario.grid(row=7, column=1, padx=10, pady=10, ipady=5)
         self.caja_usario.insert(0, usuario['n_caja'])
         self.caja_usario.config(state=tk.DISABLED)
         
         self.boton_guardar = tk.Button(lblfrme_nuevo_usuario, text='Guardar', width=10, font=('roboto', 12), bg=color.BOTON_USUARIOS, bd=0,
                                        command=self.guardar_edicion)
         self.boton_guardar.grid(row=8, column=0, ipady=5 ,pady=10,padx=30  ,sticky=tk.W)

         self.boton_cancelar = tk.Button(lblfrme_nuevo_usuario, text='cancelar', width=10, font=('roboto', 12), bg=color.BOTON_USUARIOS, bd=0,
                                            command=self.frame_edit_usario.destroy)
         self.boton_cancelar.grid(row=8, column=1, ipady=5 ,padx=30, pady=10, sticky=tk.E)

    def guardar_edicion(self):
        dni = self.txt_dni_usario.get()
        nombre = self.txt_nombre_usario.get()
        usuario = self.txt_usuario_usario.get()
        rol = self.txt_rol_usario.get()
        clave = self.txt_clave_usario.get()
        clave2 = self.txt_clave_usario2.get()
           
        caja = self.caja_usario.get()

        acceso = self.acceso_original 
        imagen = self.address_imagen  

       
        if len(dni) == 0 or len(nombre) == 0 or len(usuario) == 0 or len(rol) == 0 or len(clave) == 0 or len(clave2) == 0:
            messagebox.showerror('Error', 'Hay campos vacios')
            return
        
        validar = UsuarioValid()

        if self.usuario_original != usuario:
            if not validar.comprobar_usuario(usuario):
                messagebox.showerror('Error', 'Usuario ya existe')
                return
        
        if not validar.clave_iguales(clave, clave2):
            messagebox.showerror('Error', 'Claves diferentes')
            return
        
        editar = EditarUsuario()

        if messagebox.askokcancel('Mensaje', '¿Actualizar usuario?'):
            if editar.editar_usuario(dni, nombre, usuario, clave, rol, acceso, caja,imagen):
                messagebox.showinfo('Mensaje', 'Usuario actualizado correctamente')
                self.frame_edit_usario.destroy()
                self.update_lista()
            else:
                messagebox.showerror('Error', 'Error al actualizar el usuario')
        

        
        
        





    def delete_usuario(self, usuario, frame):
       pass
    
    def modificar_acceso(self, usuario):
       pass

    def update_lista(self):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.populate_list()