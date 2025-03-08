from APersistencia.conexion import Conexion

class Registrar(Conexion):
    def __init__(self):
        super().__init__()

    def guardar_datos(self, sql, datos):
        self.cursor.execute(sql, datos)
        self.conexion.commit()
        print(f'registros insertados : {self.cursor.rowcount}')

    def registrar_producto(self, descripcion, precio, cantidad, fecha_ven, id_categoria,imagen = 'Sinfoto', estado = True):
        datos = (descripcion, precio, cantidad, fecha_ven, id_categoria, imagen, estado)
        sql = 'insert into productos(descripcion, precio, cantidad, fecha_vencimiento, id_categoria, imagen, estado) values(%s, %s, %s, %s, %s, %s, %s)'
        
        self.guardar_datos(sql, datos)

    def registrar_categoria(self, descripcion, imagen):
        datos = (descripcion, imagen)
        sql = 'insert into categorias(descripcion, imagen) values(%s, %s)'

        self.guardar_datos(sql, datos)
   
    def registrar_moneda(self, nombre, valor):
        datos = (nombre, valor)
        sql = 'insert into monedas(nombre, valor) values(%s, %s)'

        self.guardar_datos(sql, datos)
    
    def registrar_producto_venta(self, id_producto, id_venta, cantidad, precio_unitario):
        datos = (id_producto, id_venta, cantidad, precio_unitario)
        sql = 'insert into producto_venta(id_producto, id_venta, cantidad, precio_unitario) values(%s, %s, %s, %s)'

        self.guardar_datos(sql, datos)

    def registrar_telf_usuario(self, telefono, dni):
        datos = (telefono, dni)
        sql = 'insert into telf_usarios(telefono, dni_usuario) values(%s, %s)'

        self.guardar_datos(sql, datos)

    def registrar_usuario(self, dni, nombre, usuario, clave, rol, acceso, ciudad, imagen):
        datos = (dni, nombre, usuario, clave, rol, acceso, ciudad, imagen)
        sql = 'insert into usuarios(dni, nombre, usuario, clave, rol, acceso, ciudad, imagen) values(%s,%s,%s,%s,%s,%s,%s,%s)'

        self.guardar_datos(sql,datos)

    def registar_venta(self, precio_total, fecha, moneda, dni_usuario):
        datos = (precio_total, fecha, moneda, dni_usuario)
        sql = 'insert into ventas(precio_total, fecha, moneda, dni_usuario) values(%s, %s, %s, %s)'

        self.guardar_datos(sql, datos)
        