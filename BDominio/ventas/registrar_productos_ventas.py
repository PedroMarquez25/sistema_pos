from APersistencia.servicio_registro import Registrar

class RegistrarProductoVentas():
    def __init__(self):
        self.registrar = Registrar()

    def registrar_producto_venta(self, id_venta, data):
        try:
            for producto in data:
                self.registrar.registrar_producto_venta(producto['id'], id_venta, producto['cantidad'], producto['precio'])
        except Exception as e:
            print('No se pudieron registrar los productos ventas, error en la sentencias sql')
            return False
        return True 