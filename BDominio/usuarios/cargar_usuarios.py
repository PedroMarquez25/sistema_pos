from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class CargarUsuario():
    def __init__(self):
        self.consultar_usuario = ServiciosConsultaSimple()

    def Cargar_datos_usuario(self):
        datos = []
        for usuario in self.consultar_usuario.usuarios():
            datos.append({'dni' : usuario.dni, 'nombre' : usuario.nombre, 'usuario' : usuario.usuario, 'clave' : usuario.clave,
                          'rol' : usuario.rol, 'acceso' : usuario.acceso, 'n_caja' : usuario.n_caja, 'imagen' : usuario.perfil})
        return datos
    
    def Cargar_imagen(self, usuario):
        for usuarios in self.consultar_usuario.usuarios():
            if usuarios.usuario == usuario:
                return usuarios.perfil
