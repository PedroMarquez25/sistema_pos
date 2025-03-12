from APersistencia.conexion import Conexion

class Consulta(Conexion):
    def __init__(self):
        super().__init__()
        self.consultas_simples = {'usuario' : 'select * from usuarios', 
                                  'categoria' :'select * from  categorias',
                                  'producto_venta' : 'select * from producto_venta',
                                  'producto': 'select * from productos order by id_producto',
                                  'telf_usuario' : 'select * from telf_usuario',
                                  'venta' : 'select * from ventas ORDER BY id_venta DESC', 'monedas' : 'select * from monedas'}
    
    def consulta_simple(self, tabla):
        sql = self.consultas_simples[tabla]
        self.cursor.execute(sql)
        return self.cursor.fetchall()