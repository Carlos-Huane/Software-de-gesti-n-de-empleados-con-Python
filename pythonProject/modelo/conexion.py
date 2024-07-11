import pyodbc

class Conexion:
    def __init__(self):
        self.server = 'localhost'
        self.database = 'EmpresaDB'
        self.username = 'sa'
        self.password = '12345678'
        self.con = None

    def obtener_conexion(self):
        try:
            self.con = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'UID={self.username};'
                f'PWD={self.password}'
            )
            return self.con
        except Exception as e:
            print(f"Error en la conexión: {e}")
            return None
