import webbrowser
import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from BDominio.ventas.cargar_datos_venta import DatosVenta
from BDominio.ventas.cargar_productos_venta import DatosProductoVenta

class Factura:
    def __init__(self, id_venta):
        datos_ventas = DatosVenta()
        self.venta = datos_ventas.consultar_venta_id(id_venta)

        datos_pv = DatosProductoVenta()
        self.producto_venta = datos_pv.datos_producto_venta(id_venta)
        
    def calcular_total(self):
        return sum(item['cantidad'] * item['precio'] for item in self.producto_venta)
    
    def generar_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("Helvetica", 12)
        
        # Encabezado
        c.drawString(50, 800, f"Factura N°: {self.venta['id']}")
        c.drawString(50, 780, f"Fecha: {self.venta['fecha']}")
        c.drawString(50, 760, f"Hora: {self.venta['hora']}")
        
        # Tabla de items
        y = 720
        c.drawString(50, y, "Descripción")
        c.drawString(300, y, "Cantidad")
        c.drawString(400, y, "Precio Unitario")
        c.drawString(500, y, "Total")
        y -= 20
        
        for item in self.producto_venta:
            c.drawString(50, y, item['descripcion'])
            c.drawString(300, y, str(item['cantidad']))
            c.drawString(400, y, f" Bs.{item['precio']:.2f}")
            c.drawString(500, y, f"Bs.{item['cantidad'] * item['precio']:.2f}")
            y -= 20
        
        # Total
        c.drawString(400, y-20, "Total:")
        c.drawString(500, y-20, f"Bs.{self.calcular_total():.2f}")
        
        c.save()
        
    def vista_previa(self):
        try:
            # Definir la carpeta de destino
            carpeta_destino = r"C:\Users\pedro\OneDrive\Documentos\facturas"
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Definir la ruta final del PDF
            destino = os.path.join(carpeta_destino, f"factura_{self.venta['id']}.pdf")

            # Generar el PDF directamente en la carpeta de destino
            self.generar_pdf(destino)

            # Verificar si el archivo se creó correctamente antes de abrirlo
            if os.path.exists(destino):
                print(f"Factura guardada en {destino}")
                webbrowser.open(destino)  # Abre el PDF
            else:
                print("Error: El archivo no se generó correctamente.")

        except Exception as e:
            print(f"Error en vista previa: {e}")
