from APersistencia.servicios_consulta_simple import ServiciosConsultaSimple

class CargarMoneda():
    def __init__(self):
        self.consultar = ServiciosConsultaSimple()

    def cargar_monedas(self):
        data = []
        for moneda in self.consultar.monedas():
            data.append({'nombre' : moneda.nombre, 'valor' : moneda.valor, 'simbolo' : moneda.simbolo})
        return data

    def cargar_nombres_monedas(self):
        data = []
        for moneda in self.consultar.monedas():
            data.append(moneda.nombre)
        return data
    
    def cargar_simbolo_monedas(self, n):
        data = {}
        for moneda in self.consultar.monedas():
            if n == moneda.nombre:
              data = { f'{moneda.nombre}' : moneda.simbolo} 
        return data
    
    def cargar_nombre_monedas(self, simbolo):
        for moneda in self.consultar.monedas():
            if simbolo == moneda.simbolo:
              return moneda.nombre 
