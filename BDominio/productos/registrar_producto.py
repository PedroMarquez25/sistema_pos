from APersistencia.servicio_registro import Registrar
from BDominio.productos.categorias_datos import DatosCategoria

class RegistrarProducto():
    def __init__(self):
        self.registrar_producto = Registrar()
        self.id_categoria = DatosCategoria()

    def regitrar(self, descripcion, precio, cantidad, fecha_ven, categoria, imagen, estado = True):
        try:
            precio = float(precio)
            cantidad = int(cantidad)
            fecha_ven = None if fecha_ven == '0' else fecha_ven
            categoria = self.id_categoria.id_categoria(categoria)
        except ValueError:
            print('ERROR EN LOS DATOS')
            return 1
        
        try:
            self.registrar_producto.registrar_producto(descripcion, precio, cantidad, fecha_ven, categoria, imagen, estado)
        except Exception as e:
            print('No se pudieron almacenar los datos')
            return 2
        
        return 3
