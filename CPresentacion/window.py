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
        self.title('Quicksale')
        centrar_ventana(self, cf.WIDTH , cf.HEIGHT - 100)

        self.frame_principal = Principal(self, self.mostrar_login, self.mostrar_PuntoVenta, ' ')
        self.frame_puntoVenta = PuntoVenta(self, self.mostrar_login, ' ', self.mostrar_principal)
        self.frame_registro = Registro(self,self.mostrar_login)

        self.mostrar_login()
  
    def mostrar_registro(self):
        self.frame_login.destroy()
        self.frame_registro = Registro(self, self.mostrar_login)


    def mostrar_principal(self, usuario):
        self.frame_login.destroy()
        self.frame_registro.destroy()

        self.frame_principal = Principal(self, self.mostrar_login, self.mostrar_PuntoVenta, usuario)
        
    def mostrar_login(self):
        self.frame_principal.destroy()
        self.frame_puntoVenta.destroy()
        self.frame_registro.destroy()

        self.frame_login = Login(self, self.mostrar_registro, self.mostrar_principal, self.mostrar_PuntoVenta)

    def mostrar_PuntoVenta(self, usuario):
        self.frame_login.destroy()
        self.frame_registro.destroy()
        self.frame_principal.destroy()

        self.frame_puntoVenta = PuntoVenta(self, self.mostrar_login, usuario, self.mostrar_principal)
