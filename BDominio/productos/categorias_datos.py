from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class DatosCategoria():
    def __init__(self):
        consulta = ServiciosConsultaSimple()
        self.categorias = consulta.categorias()

    def nombre_categoria(self, id):
        for categoria in self.categorias:
            if id == categoria.id_categoria:
                return categoria.descripcion
    
    def Datos_categoria(self):
        datos = []
        for categoria in self.categorias:
            datos.append(categoria.descripcion)
        return datos
    
    def id_categoria(self, descripcion):
        for categoria in self.categorias:
            if descripcion == categoria.descripcion:
                return categoria.id_categoria

