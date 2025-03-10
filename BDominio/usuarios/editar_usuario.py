from APersistencia.servicio_update import ServicioUpdate

class EditarUsuario():
    def __init__(self):
        self.actualizar = ServicioUpdate()

    def editar_usuario(self, dni, nombre, usuario, clave, rol, acceso, n_caja, imagen):
        try:
           self.actualizar.update_usuario(dni, nombre, usuario, clave, rol, acceso, n_caja, imagen)
        except Exception as e:
            print('Error en sentencia sql')
            return False
        return True