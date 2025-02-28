from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

def validar(usuario, clave):
    consulta = ServiciosConsultaSimple()
    usuarios = consulta.usuarios()
    
    for i in usuarios:
        if i.usuario == usuario and i.clave == clave:
            return True
    return False
