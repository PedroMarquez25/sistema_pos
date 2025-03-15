import tkinter as tk
import config as color

from tkinter import font, ttk, messagebox, filedialog

from BDominio.usuarios.validar_usuario import UsuarioValid
from BDominio.usuarios.guardar_usuario import GuardarUsuario

from util.util_imagenes import leer_imagen

class UsuariosRegistrar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background=color.FONDO_SEGUNDARIO)
        self.pack(fill='both', expand=True ,padx=5, pady=5)
        
        self.imagen_name = "imagenes/sinfoto.jpg"
        self.crear_widgets()

    def crear_widgets(self):
        font_awesome = font.Font(family="Font Awesome" ,size=15)
        pax, pay, ix, iy = 10, 10, 40, 8

        lbl_usuarios = tk.Label(self, text='Usuarios/registro', bg='white').place(x=5, y=5)
        lbl = tk.Label(self, text="Registrar Usuarios \uf234", font=font_awesome, bg=color.FONDO_SEGUNDARIO)
        lbl.place(x=450, y = 20)

        #=====================frame del formulario===========================================
        self.formulario = tk.Frame(self, bg=color.FONDO_SEGUNDARIO, bd=0.5, relief='groove' )
        self.formulario.place(y=80, x=160, height=500, width=790)

        #=============================widgets================================================
        lbl_informacion_general = tk.Label(self.formulario, text=' Informacion general', font='roboto 12 bold', bg=color.FONDO_SEGUNDARIO)
        lbl_informacion_general.grid(row=0,column=0,pady=10 ,sticky=tk.W)

        #dni
        lbl_dni = tk.Label(self.formulario, text='Dni', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_dni.grid(row=2,column=0, padx=pax, pady=pay, sticky=tk.W)

        self.entry_dni = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_dni.grid(row=2, column=1, padx=pax , pady=pay, ipadx=ix, ipady=iy)

        #nombre
        lbl_nombre = tk.Label(self.formulario, text='Nombre', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_nombre.grid(row=3,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_nombre = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_nombre.grid(row=3, column=1, padx=pax , pady=pay, ipadx=ix, ipady=iy)

        #usuario
        lbl_usuarios = tk.Label(self.formulario, text='Usuario', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_usuarios.grid(row=4,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_usuario = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_usuario.grid(row=4, column=1, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #clave
        lbl_clave = tk.Label(self.formulario, text='Clave', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_clave.grid(row=5,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_clave = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_clave.grid(row=5, column=1, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #repetir clave
        repetir_lbl_clave = tk.Label(self.formulario, text='Repetir clave', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        repetir_lbl_clave.grid(row=6,column=0, padx=pax, pady=pay, sticky=tk.W)
        self.entry_clave2 = ttk.Entry(self.formulario, font='roboto 12')
        self.entry_clave2.grid(row=6, column=1, padx=pax, pady=pay, ipadx=ix, ipady=iy)

        #rol
        lbl_rol_usario = tk.Label(self.formulario, text='Rol', font=('roboto', 12), bg=color.FONDO_SEGUNDARIO)
        lbl_rol_usario.grid(row=7, column=0, padx=pax, pady=pay, sticky=tk.W)
        self.txt_rol_usario = ttk.Combobox(self.formulario, values=('Cajero', 'Aministrador'), width=18,  font=('roboto', 12))
        self.txt_rol_usario.grid(row=7, column=1,padx=pax, pady=pay, ipadx=ix, ipady=iy)
        self.txt_rol_usario.current(0)

        #cargar imagen
        lbl_Cargar_imagen = tk.Label(self.formulario, text='Imagen perfil', font='roboto 12', bg=color.FONDO_SEGUNDARIO)
        lbl_Cargar_imagen.grid(row=2,column=2, pady=5, sticky=tk.NSEW)

        self.imagen = tk.Label(self.formulario)
        self.imagen.grid(row = 2, column=2, pady=5, rowspan=4)

        imag = leer_imagen('imagenes/sinfoto.jpg', (120, 120))

        self.imagen.config(image=imag)
        self.imagen.image = imag

        #botones
        self.Cargar_imagen = tk.Button(self.formulario, text='Cargar imagen' ,font=font_awesome, bg=color.BOTON_USUARIOS, width=20, height=1, bd=0,
                                       command=self.load_imagen)
        self.Cargar_imagen.grid(row=5, column=2, padx=pax, pady=20, ipady=1, sticky=tk.W)

        self.boton_guardar = tk.Button(self.formulario, text='Guardar \uf0fe',font=font_awesome ,bg=color.BOTON_USUARIOS, width=20, height=1, bd=0,
                                       command=self.registrar_usuario)
        self.boton_guardar.grid(row=9, column=0, padx=pax, pady=20, ipady=1, sticky=tk.E)

        self.boton_limpiar = tk.Button(self.formulario, text='Limpiar campos',font=font_awesome  ,bg=color.BOTON_USUARIOS, width=20, height=1, bd=0,
                                       command=self.limpiar_campos)
        self.boton_limpiar.grid(row=9, column=1, padx=pax, pady=20, ipady=1 ,sticky=tk.W)

    def registrar_usuario(self):
        valid_user = UsuarioValid()
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        rol = self.txt_rol_usario.get()
        usuario = self.entry_usuario.get()
        clave1 = self.entry_clave.get()
        clave2 = self.entry_clave2.get()
        imagen = self.imagen_name

        if self.campos_vacios(dni, nombre, usuario, clave1, clave2) and valid_user.comprobar_dni(dni) and valid_user.clave_iguales(clave1, clave2) and valid_user.comprobar_usuario(usuario):
            guardar = GuardarUsuario()

            try:
                dni = int(dni)
            except Exception as e:
                messagebox.showerror('Error', 'Dni contiene valores no numericos')
                return 0

            if messagebox.askyesno(title='Mensaje', message='¿Registrar usuario?'):
                if guardar.guardar_datos(dni, nombre, usuario, clave1, rol, imagen):
                    messagebox.showinfo(title='Mensaje', message='Usuario creado correctamente')
                    self.limpiar_campos()
                else:
                    messagebox.showerror(title='Mensaje', message='Error inesperado')
        else:
            if not self.campos_vacios(dni, nombre, usuario, clave1, clave2):
                messagebox.showerror(title='Mensaje', message='Hay campos Vacios')
            elif not valid_user.comprobar_dni(dni):
                messagebox.showerror(title='Mensajes', message='Usuario ya existe')
            elif not valid_user.clave_iguales(clave1, clave2):
                messagebox.showerror(title='Mensaje', message='Contraseñas no coinciden')
            elif not valid_user.comprobar_usuario(usuario):
                messagebox.showerror(title='Mensaje', message='Usuario exixtente')
               
    def load_imagen(self):
        file_path = filedialog.askopenfilename() #abre cuadro de dialogo
        if file_path:
            try:
                imag = leer_imagen(file_path, (120, 120))
            except Exception as e:
                messagebox.showerror('Error', 'Error al cargar la imagen')
                file_path = "imagenes/sinfoto.jpg"
                imag = leer_imagen("imagenes/sinfoto.jpg", (120, 120))
            self.imagen.config(image=imag)
            self.imagen.image = imag
            self.imagen_name = file_path
            
    def limpiar_campos(self):
        self.entry_dni.delete(0,'end')
        self.entry_nombre.delete(0,'end')
        self.txt_rol_usario.delete(0,'end')
        self.entry_usuario.delete(0,'end')
        self.entry_clave.delete(0,'end')
        self.entry_clave2.delete(0,'end')
        self.imagen_name = "imagenes/sinfoto.jpg"
        imag = leer_imagen(self.imagen_name, (120,120))
        self.imagen.config(image=imag)
        self.imagen.image = imag

    def campos_vacios(self, dni, nombre, usuario, clave1, clave2):
        return True if len(dni) != 0 and len(nombre) != 0 and len(usuario) != 0 and clave1 != 0 and clave2 !=0 else False