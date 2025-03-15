from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

from BDominio.productos.cargar_producto import CargarProductos

class DatosProductoVenta():
    def __init__(self):
        self.consultar = ServiciosConsultaSimple()
        self.desc_producto = CargarProductos()
    
    def datos_producto_venta(self, id_venta):
        productos = []  
        for producto in self.consultar.producto_venta():
            if producto.id_venta == id_venta:
                productos.append({'id_venta' : producto.id_venta, 'id_producto' : producto.id_producto, 'precio' : producto.precio_unitario, 'cantidad' : producto.cantidad, 'descripcion' : self.desc_producto.nombre_producto(producto.id_producto)})
        return productos