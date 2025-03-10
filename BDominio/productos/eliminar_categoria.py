from APersistencia.servicio_eliminacion import ServicioDelete

class EliminarCategoria():
    def __init__(self):
        self.eliminar = ServicioDelete()

    def eliminar_categoria(self, id):
        try:
            self.eliminar.delete_categoria(id)
        except Exception as e:
            print('Error con la conexion a la base de datos')
            return False
        return True