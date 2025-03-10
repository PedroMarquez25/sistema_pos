from APersistencia.servicio_update import ServicioUpdate

class EditarCategoria():
    def __init__(self):
        self.actualizar = ServicioUpdate()
    
    def actualizar_categoria(self, id, descripcion, imagen):
        try:
            self.actualizar.update_categoria(id, descripcion, imagen)
        except Exception as e:
            print('Problemas con la base de dtaos al actualizar la categoria')
            return False
        return True