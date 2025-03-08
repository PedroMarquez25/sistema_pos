from APersistencia.conexion import Conexion

class ServicioDelete(Conexion):
    def __init__(self):
        super().__init__()
    
    def delete_producto(self, id_producto):
        sql = 'Delete from productos where id_producto = %s'
        self.cursor.execute(sql, (id_producto,))
        self.conexion.commit()   
    def delete_usuario(self, dni_usuario):
        sql = 'delete from usuarios where dni = %s'
        self.cursor.execute(sql, (dni_usuario, ))
        self.conexion.commit()
    def delete_venta(self, id_venta):
        sql = 'delete from ventas where id_venta = %s'
        self.cursor.execute(sql, (id_venta, ))
        self.conexion.commit()
    def delete_categoria(self, id_categoria):
        sql = 'delete from categorias where id_categoria = %s'
        self.cursor.execute(sql, (id_categoria,))
        self.conexion.commit()
    def delete_moneda(self, nombre):
        sql = 'delete from monedas where nombre = %s'
        self.cursor.execute(sql, (nombre,))
        self.conexion.commit()
    def delete_telefono(self, numero, dni):
        sql = 'delete from telf_usuarios where telefono = %s and dni_usuario = %s'
        self.cursor.execute(sql, (numero, dni))
        self.conexion.commit()