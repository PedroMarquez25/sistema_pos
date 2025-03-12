import datetime
from APersistencia.servicio_registro import Registrar

class Registrar_venta():
    def __init__(self):
        self.registrar = Registrar()

    def guardar_venta(self,precio_total,fecha ,moneda, hora):
        try:
            self.registrar.registar_venta(precio_total, fecha, moneda, hora)
        except Exception as e:
            print('Error en la sentecia sql de registrar venta')
            return False
        return True