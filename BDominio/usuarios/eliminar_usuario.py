from APersistencia.servicio_eliminacion import ServicioDelete

class EliminarUsuario():
    def __init__(self):
        self.eliminar = ServicioDelete()

    def eliminar_usuario(self, dni):
        try:
            self.eliminar.delete_usuario(dni)
        except Exception as e:
            print('Error en la sentencia delete')
            return False
        return True