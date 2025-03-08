from APersistencia.servicio_eliminacion import ServicioDelete

class EliminarProducto():
    def __init__(self):
        self.delete = ServicioDelete()

    def delete_producto(self, id):
        try:
            self.delete.delete_producto(id)
        except Exception as e:
            print('Error al eliminar el producto {e}')
            return False
        return True