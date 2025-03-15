from APersistencia import modelos
from APersistencia.consulta import Consulta

class ServiciosConsultaSimple(Consulta):
    def __init__(self):
        super().__init__()

    def productos(self):
        productos = []

        for i in self.consulta_simple('producto'):
            id, descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado = i 
            productos.append(modelos.Productos(id, descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado))
        
        return productos
    
    def ventas(self):
        ventas = []

        for i in self.consulta_simple('venta'):
            id, precio, fecha, moneda, hora, dni_usuario = i
            ventas.append(modelos.Ventas(id, precio, fecha, moneda, hora, dni_usuario))

        return ventas

    def categorias(self):
        categorias = []

        for i in self.consulta_simple('categoria'):
            id, descripcion, imagen = i 
            categorias.append(modelos.Categorias(id, descripcion, imagen))
        
        return categorias

    def monedas(self):
        monedas = []

        for i in self.consulta_simple('monedas'):
            nombre, valor, simbolo = i
            monedas.append(modelos.Monedas(nombre, valor, simbolo))

        return monedas

    def producto_venta(self):
        producto_venta = []

        for i in self.consulta_simple('producto_venta'):
            id_producto, id_venta, cantidad, precio_unitario = i
            producto_venta.append(modelos.Producto_venta(id_producto, id_venta, cantidad, precio_unitario))

        return producto_venta

    def usuarios(self):
        usuarios = []

        for i in self.consulta_simple('usuario'):
            dni, nombre, usuario, clave, rol, acceso, n_caja, imagen = i 
            usuarios.append(modelos.Usuarios(dni, nombre, usuario, clave, rol, acceso, n_caja, imagen ))

        return usuarios