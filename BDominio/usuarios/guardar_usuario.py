from APersistencia.servicio_registro import Registrar

class GuardarUsuario():
    def __init__(self):
        self.nuevo_usuario = Registrar().registrar_usuario

    def guardar_datos(self, dni, nombre, usuario, clave, rol,imagen = '--'):
        acceso = 1 if rol == 'Cajero' else 2
        try:
            self.nuevo_usuario(dni, nombre, usuario, clave, rol, acceso, imagen )
        except:
            return False
        
        return True


    
    
