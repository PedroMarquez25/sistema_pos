from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class DatosVenta():
    def __init__(self):
        self.consultar = ServiciosConsultaSimple()

    def consultar_venta_id(self, id_venta):
        for venta in self.consultar.ventas():
             if venta.id_venta == id_venta:
                 dicc = {'id' : venta.id_venta, 'fecha' : venta.fecha, 'moneda' : venta.moneda, 'precio_total' : venta.precio_total, 'hora' : venta.hora, 'dni_usuario' : venta.dni_usuario}
                 return dicc
             
    def consultar_ventas(self):
        data = []
        for venta in self.consultar.ventas():
            data.append({'id' : venta.id_venta, 'fecha' : venta.fecha, 'moneda' : venta.moneda, 'precio_total' : venta.precio_total, 'hora' : venta.hora, 'dni_usuario' : venta.dni_usuario})
        return data