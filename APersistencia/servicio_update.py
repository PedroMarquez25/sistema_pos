from APersistencia.conexion import Conexion

class ServicioUpdate(Conexion):
    def __init__(self):
        super().__init__()
    
    def update_categoria(self, id, desc, img):
        sql = 'update categorias set descripcion = %s, imagen = %s where id_categoria = %s'
        self.cursor.execute(sql, (desc, img, id))
        self.conexion.commit()
    def update_moneda(self, nombre, valor):
        sql = 'update monedas set valor = %s where nombre = %s'
        self.cursor.execute(sql, (valor, nombre))
        self.conexion.commit()
    def update_producto(self, id, desc, precio, cant, fecha_ven, id_categoria, imagen, estado):
        sql = 'update productos set descripcion = %s, precio = %s, cantidad = %s, fecha_vencimiento = %s, id_categoria = %s, imagen = %s, estado = %s where id_producto = %s'
        self.cursor.execute(sql, (desc, precio, cant, fecha_ven, id_categoria, imagen, estado,id))
        self.conexion.commit()

    def update_usuario(self, dni, nombre, usuario, clave, rol, acceso, n_caja, imagen):
        sql = 'update usuarios set nombre = %s, usuario = %s, clave = %s, rol = %s, acceso = %s, n_caja = %s, imagen =  %s where dni = %s'
        self.cursor.execute(sql, (nombre, usuario, clave, rol, acceso, n_caja, imagen, dni))
        self.conexion.commit()

    def reponer_producto(self, id, cantidad):
        sql = 'update productos set cantidad = cantidad + %s where id_producto = %s'
        self.cursor.execute(sql, (cantidad, id))
        self.conexion.commit()