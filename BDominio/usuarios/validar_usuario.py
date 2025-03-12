from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class UsuarioValid:
    def __init__(self):
         self.consulta = ServiciosConsultaSimple()
         self.usuarios = self.consulta.usuarios()
        
    #verificar acceso para entrar en la aplicacion
    def validar(self, usuario, clave):   
        retorno = 0
        
        for i in self.usuarios:
            if i.usuario == usuario and i.clave == clave:            
                retorno = i.acceso
                break

        return retorno
    
    def acceso(self, usuario):
        for i in self.usuarios:
            if i.usuario == usuario:
                return i.acceso

    def clave_iguales(self, clave1, clave2):
        return True if clave2 == clave1 else False
    
    def comprobar_dni(self, dni):
        for i in self.usuarios:
            if i.dni == dni:
                return False
        return True

    def comprobar_usuario(self, usuario):
        for i in self.usuarios:
            if i.usuario == usuario:
                return False
        return True
    
    def codigo_registro(self, codigo):
        return True if codigo == '123456789' else False