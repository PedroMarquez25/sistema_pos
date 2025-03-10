from APersistencia.servicio_registro import Registrar

class RegistrarCategoria():
    def __init__(self):
        self.registrar = Registrar()

    def registrar_categoria(self, descripcion, imagen):
        try:
            self.registrar.registrar_categoria(descripcion, imagen)
        except Exception as e:
            print('Problemas con la conexion a la base de datos')
            return False
        return True