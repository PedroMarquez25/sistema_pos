import tkinter as tk
import config as cf
from util.util_ventana import centrar_ventana
from CPresentacion.principal import Principal
from CPresentacion.registro import Registro
from CPresentacion.login import Login
from CPresentacion.punto_venta import PuntoVenta

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()

        self.frames = {}

        self.frame_principal = Principal(self, self.mostrar_login, self.mostrar_PuntoVenta)
        self.frame_registro = Registro(self, self.mostrar_principal, self.mostrar_login)
        self.frame_login = Login(self, self.mostrar_registro, self.mostrar_principal,self.mostrar_PuntoVenta)
        self.frame_PuntoVenta = PuntoVenta(self,self.mostrar_login)

        self.frames[Principal] = self.frame_principal
        self.frames[Registro] = self.frame_registro
        self.frames[Login] = self.frame_login
        self.frames[PuntoVenta] = self.frame_PuntoVenta

        self.mostrar_frame(Login)

    def mostrar_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def mostrar_registro(self):
        self.mostrar_frame(Registro)

    def mostrar_principal(self):
        self.mostrar_frame(Principal)
        
    def mostrar_login(self):
        self.mostrar_frame(Login)

    def mostrar_PuntoVenta(self):
        self.mostrar_frame(PuntoVenta)

    def config_window(self):
        self.title('Quicksale')
        w, h = cf.WIDTH - 100, cf.HEIGHT - 100
        centrar_ventana(self,w,h)
        

 