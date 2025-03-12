from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class VentaReciente():
    def __init__(self):
        self.consultar = ServiciosConsultaSimple()

    def venta_reciente(self, fecha, hora, precio_total):
        try:
            for venta in self.consultar.ventas():
                if str(venta.fecha) == str(fecha) and str(venta.hora) == str(hora) and str(venta.precio_total) == str(precio_total):
                    return venta.id_venta
        except Exception as e:
            print('error en la sentencia sql de consultar ventas')
            return False
        

        