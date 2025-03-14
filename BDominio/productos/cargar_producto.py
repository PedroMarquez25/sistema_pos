import re

from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

from BDominio.productos.categorias_datos import DatosCategoria

class CargarProductos():
    def __init__(self):
        self.consulta = ServiciosConsultaSimple()
        self.categoria = DatosCategoria()
         
    def cargar_datos_consulta(self):
        data = []
        for producto in self.consulta.productos():
            data.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                         'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                         'fecha' : producto.fecha_vencimiento})
        return data
    
    def cargar_productos_activos(self):
        data = []
        for producto in self.consulta.productos():
            if producto.estado and producto.cantidad > 0:
                data.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                         'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                         'fecha' : producto.fecha_vencimiento})
        return data
    
    def buscar_producto_id(self, id):
        try:
            id = int(id)
            busqueda = []
        except ValueError:
            return False
    
        for producto in self.consulta.productos():
            if producto.id_producto == id:
                busqueda = [{"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                             'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                            'fecha' : producto.fecha_vencimiento}]
        return busqueda
    
    def buscar_producto_id_activo(self, id):
        try:
            id = int(id)
            busqueda = []
        except ValueError:
            return False
        
        for producto in self.consulta.productos():
            if producto.id_producto == id and producto.estado:
                busqueda = [{"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                             'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                            'fecha' : producto.fecha_vencimiento}]
        return busqueda
    
    def buscar_producto_desc(self, desc):
        busqueda = []
        for producto in self.consulta.productos():
            if self.contiene_patron(producto.descripcion, desc):
                busqueda.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                             'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                            'fecha' : producto.fecha_vencimiento})
        return busqueda
    
    def buscar_producto_desc_activo(self, desc):
        busqueda = []
        for producto in self.consulta.productos():
            if self.contiene_patron(producto.descripcion, desc) and producto.estado:
                busqueda.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                             'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                            'fecha' : producto.fecha_vencimiento})
        return busqueda
            
    def producto_por_categoria(self, id):
        numero = 0
        for producto in self.consulta.productos():
            if producto.id_categoria == id:
                numero += 1
        return numero
    
    def productos_categoria(self, id):
        data = []
        for producto in self.consulta.productos():
            if producto.id_categoria == id:
                data.append({"id" : producto.id_producto, 'desc' : producto.descripcion, 'precio' : producto.precio, 'cantidad' : producto.cantidad, 
                         'categoria': self.categoria.nombre_categoria(producto.id_categoria), 'estado' : producto.estado, 'imagen' : producto.imagen,
                         'fecha' : producto.fecha_vencimiento})
        return data
    
    def nombre_producto(self, id):
        for producto in self.consulta.productos():
            if producto.id_producto == id:
                return producto.descripcion

    def contiene_patron(self, cadena, patron):
         return bool(re.search(patron.lower(), cadena.lower()))