import tkinter as tk
import config as colores

from BDominio.usuarios.validar_usuario import UsuarioValid
from BDominio.usuarios.guardar_usuario import GuardarUsuario
from tkinter import ttk, messagebox, font
from util.util_ventana import centrar_ventana

class Registro(tk.Frame):
    def __init__(self, parent, mostrar_login):
        super().__init__(parent)
        self.configure(background=colores.COLOR_SEGUNDARIO)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.mostrar_login = mostrar_login
        self.font_awesome = font.Font(family="Font Awesome 6 Free Solid" ,size=35)

        self.crear_formulario()
        self.crear_widgets()
        
    def crear_formulario(self):
        self.formulario = tk.Frame(self, width=400, height=400, bg=colores.COLOR_PRINCIPAL, bd=0)
        self.formulario.pack(pady=160)
        self.formulario.pack_propagate(False)
    
    def crear_widgets(self):
        self.frame_titulo = tk.Frame(self.formulario, bg=colores.COLOR_PRINCIPAL, height=100)
        self.frame_titulo.pack(side='top',fill='x')

        self.frame_codigo = tk.Frame(self.formulario, bg=colores.COLOR_PRINCIPAL, height=200)
        self.frame_codigo.pack(side='top',fill='x')

        #==================================titulo========================================================================
        label_titulo = tk.Label(self.frame_titulo, text='Registrarse', font=('Montserrat',20, 'bold'), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        label_titulo.pack(pady=10)
 
        icono = tk.Label(self.frame_titulo, text='\uf509', font=self.font_awesome, bg=colores.COLOR_SEGUNDARIO, fg=colores.COLOR_TEXTO)
        icono.pack(pady=5)

        #================================Label y campo codigo============================================================
        label_codigo = tk.Label(self.frame_codigo, text='Codigo de registro' ,font=('roboto', 14),
                                    fg=colores.COLOR_TEXTO, bg=colores.COLOR_PRINCIPAL ,anchor='w')
        label_codigo.pack(fill='x', padx=30, pady=2, ipady=5)

        self.entry_codigo = ttk.Entry(self.frame_codigo, font=('time', 18), show="*")
        self.entry_codigo.pack(fill='x', padx=30,pady=5 ,ipady=5)

        #================================Boton de registrar y regresar===========================================

        self.boton_registrar = tk.Button(self.frame_codigo, text='Registrar', width=15,height=1, font=('Roboto', 14),
                                          bd=0, bg=colores.BOTON_PRODUCTOS, command=self.nuevo_usuario)
        self.boton_registrar.pack(pady=10, ipady=2)

        self.boton_regresar = tk.Button(self.frame_codigo, text='Regresar', width=12,height=1, font=('Roboto', 14),
                                          bd=0, bg=colores.BOTON_PRODUCTOS, command=self.mostrar_login)
        self.boton_regresar.pack(pady=5, ipady=2)

    def nuevo_usuario(self):
        valid_user = UsuarioValid()

        if len(self.entry_codigo.get()) == 0:
            messagebox.showerror(title='Mensaje', message='Campo de texto vacio')
            return 0

        if not valid_user.codigo_registro(self.entry_codigo.get()):
            messagebox.showerror(title='Mensaje', message='Codigo de registro incorrecto')
            return 0
        #=============================Ventana emergente===================================================
        self.frame_nuevo_usario = tk.Toplevel(self)
        self.frame_nuevo_usario.title('Nuevo usuario')
        self.frame_nuevo_usario.geometry(centrar_ventana(self.frame_nuevo_usario, 450, 600))
        self.frame_nuevo_usario.resizable(0,0)
        self.frame_nuevo_usario.grab_set()
        self.frame_nuevo_usario.config(bg=colores.COLOR_PRINCIPAL)

        lbl_titulo = tk.Label(self.frame_nuevo_usario, text="Nuevo usuario", font=('Lato', 18), bg=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_titulo.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=5)

        lbl_icono = tk.Label(self.frame_nuevo_usario, text="\uf234", font=self.font_awesome, bg=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO )
        lbl_icono.grid(row=1, column=0, padx=10, pady=5)

        #===========================Formulario de registro============================================
        lblfrme_nuevo_usuario = tk.LabelFrame(self.frame_nuevo_usario, text='Datos personales' ,bg=colores.COLOR_PRINCIPAL, bd=0.5, fg=colores.COLOR_TEXTO)
        lblfrme_nuevo_usuario.grid(row=2, column=0, sticky=tk.NSEW, padx=30, pady=15)


        lbl_dni_usario = tk.Label(lblfrme_nuevo_usuario, text='DNI', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_dni_usario.grid(row=0, column=0, padx=10, pady=10)
        self.txt_dni_usario = ttk.Entry(lblfrme_nuevo_usuario, width=20,  font=('roboto', 12))
        self.txt_dni_usario.grid(row=0, column=1, padx=10, pady=10, ipady=5)

        lbl_nombre_usario = tk.Label(lblfrme_nuevo_usuario, text='Nombre', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_nombre_usario.grid(row=1, column=0, padx=10, pady=10)
        self.txt_nombre_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
        self.txt_nombre_usario.grid(row=1, column=1, padx=10, pady=10, ipady=5)

        lbl_rol_usario = tk.Label(lblfrme_nuevo_usuario, text='Rol', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_rol_usario.grid(row=2, column=0, padx=10, pady=10)
        self.txt_rol_usario = ttk.Combobox(lblfrme_nuevo_usuario, values=('Cajero', 'Aministrador'), width=18,  font=('roboto', 12))
        self.txt_rol_usario.grid(row=2, column=1, padx=10, pady=10, ipady=5)
        self.txt_rol_usario.current(0)

        lbl_usuario_usario = tk.Label(lblfrme_nuevo_usuario, text='Usuario', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_usuario_usario.grid(row=4, column=0, padx=10, pady=10)
        self.txt_usuario_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12))
        self.txt_usuario_usario.grid(row=4, column=1, padx=10, pady=10, ipady=5)

        lbl_clave_usario = tk.Label(lblfrme_nuevo_usuario, text='Contraseña', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_clave_usario.grid(row=5, column=0, padx=10, pady=10)
        self.txt_clave_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12), show="*")
        self.txt_clave_usario.grid(row=5, column=1, padx=10, pady=10, ipady=5)

        lbl_clave2_usario = tk.Label(lblfrme_nuevo_usuario, text='Repetir contraseña', font=('roboto', 12), background=colores.COLOR_PRINCIPAL, fg=colores.COLOR_TEXTO)
        lbl_clave2_usario.grid(row=6, column=0, padx=10, pady=10)
        self.txt_clave2_usario = ttk.Entry(lblfrme_nuevo_usuario,width=20,  font=('roboto', 12), show="*")
        self.txt_clave2_usario.grid(row=6, column=1, padx=10, pady=10, ipady=5)
            
        self.boton_guardar = tk.Button(lblfrme_nuevo_usuario, text='Guardar', width=10, font=('roboto', 12), bg=colores.BOTON_PRODUCTOS, bd=0,
                                    command=self.guardar_usuario)
        self.boton_guardar.grid(row=7, column=0, ipady=5 ,pady=10, sticky=tk.S,)

        self.boton_cancelar = tk.Button(lblfrme_nuevo_usuario, text='cancelar', width=10, font=('roboto', 12), bg=colores.BOTON_PRODUCTOS, bd=0,
                                        command=self.frame_nuevo_usario.destroy)
        self.boton_cancelar.grid(row=7, column=1, ipady=5 ,padx=5, pady=10, sticky=tk.N)
               
    def guardar_usuario(self):
        valid_user = UsuarioValid()

        dni = self.txt_dni_usario.get()
        nombre = self.txt_nombre_usario.get()
        rol = self.txt_rol_usario.get()
        usuario = self.txt_usuario_usario.get()
        clave1 = self.txt_clave_usario.get()
        clave2 = self.txt_clave2_usario.get()

        if self.campos_vacios(dni, nombre, usuario, clave1, clave2) and valid_user.comprobar_dni(dni) and valid_user.clave_iguales(clave1, clave2) and valid_user.comprobar_usuario(usuario):
            guardar = GuardarUsuario()

            try:
                dni = int(dni)
            except Exception as e:
                messagebox.showerror('Error', 'Dni contiene valores no numericos')
                return 0

            if messagebox.askretrycancel(title='Mensaje', message='¿Registrar usuario?', parent = self.frame_nuevo_usario):
                if guardar.guardar_datos(dni, nombre, usuario, clave1, rol):
                    messagebox.showinfo(title='Mensaje', message='Usuario creado correctamente', parent = self.frame_nuevo_usario)
                    self.frame_nuevo_usario.destroy()
                    
                else:
                    messagebox.showerror(title='Mensaje', message='Error inesperado', parent = self.frame_nuevo_usario)
        else:
            if not self.campos_vacios(dni, nombre, usuario, clave1, clave2):
                messagebox.showerror(title='Mensaje', message='Hay campos Vacios', parent = self.frame_nuevo_usario)
            elif not valid_user.comprobar_dni(dni):
                messagebox.showerror(title='Mensajes', message='Usuario ya existe', parent = self.frame_nuevo_usario)
            elif not valid_user.clave_iguales(clave1, clave2):
                messagebox.showerror(title='Mensaje', message='Contraseñas no coinciden', parent = self.frame_nuevo_usario)
            elif not valid_user.comprobar_usuario(usuario):
                messagebox.showerror(title='Mensaje', message='Usuario exixtente', parent = self.frame_nuevo_usario)
               
    def campos_vacios(self, dni, nombre, usuario, clave1, clave2):
        return True if len(dni) != 0 and len(nombre) != 0 and len(usuario) != 0 and clave1 != 0 and clave2 !=0 else False
  