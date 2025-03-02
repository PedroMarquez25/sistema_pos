from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class UsuarioValid:
    def __init__(self):
         self.consulta = ServiciosConsultaSimple()

    def validar(self, usuario, clave):    
        usuarios = self.consulta.usuarios()
        retorno = 0
        
        for i in usuarios:
            if i.usuario == usuario and i.clave == clave:            
                retorno = i.acceso
                break

        return retorno
              
               
