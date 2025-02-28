import psycopg2

class Conexion:

    def __init__(self):
        self.conexion = psycopg2.connect(user = 'Admin', password = '31315691', host = 'localhost', port = '5432', database = 'bd_pos')
        self.cursor = self.conexion.cursor()

    def __del__(self):
        self.cursor.close()
        self.conexion.close()