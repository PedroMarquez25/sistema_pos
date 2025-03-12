class Categorias:
    def __init__(self, id_categoria, descripcion, imagen):
        self.id_categoria = id_categoria
        self.descripcion = descripcion
        self.imagen = imagen

    def print(self):
        print(f'{self.id_categoria} {self.descripcion}')


class Monedas:
    def __init__(self, nombre, valor, simbolo):
        self.nombre = nombre
        self.valor = valor
        self.simbolo = simbolo
    
    
class Producto_venta:
    def __init__(self, id_producto, id_venta, cantidad, precio_unitario ):
        self.id_producto = id_producto
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def print(self):
        print(f'{self.id_producto} {self.id_venta} {self.cantidad} {self.precio_unitario}')


class Productos:
    def __init__(self, id_producto, descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_ven
        self.id_categoria = id_categoria
        self.imagen = imagen
        self.estado = estado

    def print(self):
        print(f'{self.id_producto} {self.descripcion} {self.precio} {self.cantidad} {self.fecha_vencimiento} {self.id_categoria}')


class Telf_admi:
    def __init__(self, telefono, dni_usuario):
        self.telefono = telefono
        self.dni_usuario = dni_usuario
    
    def print(self):
        print(f"{self.telefono} {self.dni_usuario}")


class Usuarios:
    def __init__(self, dni, nombre, usuario, clave, rol, acceso, n_cajero, imagen_perfil):
        self.dni= dni
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.rol = rol
        self.acceso = acceso
        self.n_caja = n_cajero
        self.perfil = imagen_perfil
         
        

class Ventas:
    def __init__(self, id_venta, precio_total, fecha, moneda, hora):
        self.id_venta = id_venta
        self.precio_total = precio_total
        self.fecha = fecha
        self.moneda = moneda
        self.hora = hora

