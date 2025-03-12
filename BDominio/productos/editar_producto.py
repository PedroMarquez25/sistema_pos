from APersistencia.servicio_update import ServicioUpdate

class EditarProducto():
    def __init__(self):
        self.Editar = ServicioUpdate()

    def editar_producto(self, id, desc, precio, cant, fecha_ven, id_categoria, imagen ,estado):
        try:
            precio = float(precio)
            cant = int(cant)
            id_categoria = int(id_categoria)
            fecha_ven = None if fecha_ven == '0' else fecha_ven
        except ValueError as e:
            print('Datos inconpatible')
            return False
        
        try:
            self.Editar.update_producto(id, desc, precio, cant, fecha_ven, id_categoria, imagen, estado)
        except Exception as e:
            print('Error al actualizar los datos {e}')
            print(fecha_ven)
            return False
        
        return True
    
    def reponer_producto(self, id, cantidad):
        try:
            cantidad = int(cantidad)
        except Exception as e:
            print('Error Datos incopatibles')
            return False
        
        try:
            self.Editar.reponer_producto(id, cantidad)
        except Exception as e:
            print('Error en la sentencia sql')
            return
        
        return True

    def disminuir_producto(self, datos):
        try:
            for producto in datos:
                self.Editar.disminuir_producto(producto['id'], producto['cantidad'])
        except Exception as e:
            print('error al actualizar cantidad')
            return False
        return True


          
            

