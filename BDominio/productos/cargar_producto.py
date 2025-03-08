from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple
from BDominio.productos.categorias_datos import DatosCategoria

class CargarProductos():
    def __init__(self):
        self.consulta = ServiciosConsultaSimple()
        self.categoria = DatosCategoria()
         
    
    def cargar_datos_consulta(self):
        try:
            productos = self.consulta.productos()
        except:
            print('Problemas con la bases de datos')

        data = []
        for producto in productos:
            data.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                         'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                         'fecha' : producto.fecha_vencimiento})
        return data
        
