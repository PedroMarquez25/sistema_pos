from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import tempfile
import os
import webbrowser

class Factura:
    def __init__(self, numero, cliente, items):
        self.numero = numero
        self.cliente = cliente
        self.items = items
        self.fecha = datetime.now().strftime("%d/%m/%Y")
        
    def calcular_total(self):
        return sum(item['cantidad'] * item['precio'] for item in self.items)
    
    def generar_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("Helvetica", 12)
        
        # Encabezado
        c.drawString(50, 800, f"Factura N°: {self.numero}")
        c.drawString(50, 780, f"Cliente: {self.cliente}")
        c.drawString(50, 760, f"Fecha: {self.fecha}")
        
        # Tabla de items
        y = 720
        c.drawString(50, y, "Descripción")
        c.drawString(300, y, "Cantidad")
        c.drawString(400, y, "Precio Unitario")
        c.drawString(500, y, "Total")
        y -= 20
        
        for item in self.items:
            c.drawString(50, y, item['descripcion'])
            c.drawString(300, y, str(item['cantidad']))
            c.drawString(400, y, f"${item['precio']:.2f}")
            c.drawString(500, y, f"${item['cantidad'] * item['precio']:.2f}")
            y -= 20
        
        # Total
        c.drawString(400, y-20, "Total:")
        c.drawString(500, y-20, f"${self.calcular_total():.2f}")
        
        c.save()
        
    def vista_previa(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_filename = temp_file.name
        self.generar_pdf(temp_filename)
        webbrowser.open(temp_filename)
        
        opcion = input("¿Desea guardar la factura? (s/n): ")
        if opcion.lower() == 's':
            destino = input("Ingrese el nombre del archivo para guardar (ejemplo: factura_001.pdf): ")
            os.rename(temp_filename, destino)
            print(f"Factura guardada como {destino}")
        else:
            os.remove(temp_filename)
            print("Factura descartada.")

# Ejemplo de uso
items = [
    {"descripcion": "Producto A", "cantidad": 2, "precio": 10.50},
    {"descripcion": "Producto B", "cantidad": 1, "precio": 25.75},
    {"descripcion": "Servicio C", "cantidad": 3, "precio": 15.00}
]

factura = Factura("001", "Cliente XYZ", items)
factura.vista_previa()
