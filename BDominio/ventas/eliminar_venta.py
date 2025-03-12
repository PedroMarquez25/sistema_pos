from APersistencia.servicio_eliminacion import ServicioDelete

class EliminarVenta():
    def __init__(self):
        self.eliminar = ServicioDelete()

    def eliminar_venta(self, id_venta):
        try:
            self.eliminar.delete_venta(id_venta)
        except Exception as e:
            print('Error al eliminar en la sentencia')
            return False
        return True