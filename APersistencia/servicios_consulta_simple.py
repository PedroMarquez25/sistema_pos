from APersistencia import modelos
from APersistencia.consulta import Consulta

class ServiciosConsultaSimple(Consulta):
    def __init__(self):
        super().__init__()

    def productos(self):
        productos = []

        registros = self.consulta_simple('producto')

        for i in registros:
            id, descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado = i 
            productos.append(modelos.Productos(id, descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado))
        
        return productos
    
    def ventas(self):
        ventas = []

        registros = self.consulta_simple('venta')

        for i in registros:
            id, precio, fecha, moneda, hora = i
            ventas.append(modelos.Ventas(id, precio, fecha, moneda, hora))

        return ventas

    def categorias(self):
        categorias = []

        registros = self.consulta_simple('categoria')

        for i in registros:
            id, descripcion, imagen = i 
            categorias.append(modelos.Categorias(id, descripcion, imagen))
        
        return categorias

    def monedas(self):
        monedas = []

        registros = self.consulta_simple('monedas')

        for i in registros:
            nombre, valor, simbolo = i
            monedas.append(modelos.Monedas(nombre, valor, simbolo))

        return monedas

    def producto_venta(self):
        producto_venta = []

        registros = self.consulta_simple('producto_venta')

        for i in registros:
            id_producto, id_venta, cantidad, precio_unitario = i
            producto_venta.append(modelos.Producto_venta(id_producto, id_venta, cantidad, precio_unitario))

        return producto_venta

    def telf_usuarios(self):
        telefonos = []

        registros = self.consulta_simple('telf_usuario')

        for i in registros:
            telf, dni = i
            telefonos.append(modelos.Telf_admi(telf,dni))
        
        return telefonos

    def usuarios(self):
        usuarios = []

        registros = self.consulta_simple('usuario')

        for i in registros:
            dni, nombre, usuario, clave, rol, acceso, n_caja, imagen = i 
            usuarios.append(modelos.Usuarios(dni, nombre, usuario, clave, rol, acceso, n_caja, imagen ))

        return usuarios