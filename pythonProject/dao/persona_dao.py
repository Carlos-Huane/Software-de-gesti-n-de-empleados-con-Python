from modelo.conexion import Conexion
class PersonaDAO:
    def __init__(self):
        self.conexion = Conexion()

    def agregar_persona(self, nombre):
        con = self.conexion.obtener_conexion()
        if con is not None:
            try:
                query = "INSERT INTO Personas (nombre) VALUES (?)"
                cursor = con.cursor()
                cursor.execute(query, (nombre,))
                con.commit()
                con.close()
                return True
            except Exception as e:
                print(f"Error al agregar persona: {e}")
                return False
        return False

    def eliminar_persona(self, nombre):
        con = self.conexion.obtener_conexion()
        if con is not None:
            try:
                query = "DELETE FROM Personas WHERE nombre = ?"
                cursor = con.cursor()
                cursor.execute(query, (nombre,))
                con.commit()
                con.close()
                return True
            except Exception as e:
                print(f"Error al eliminar persona: {e}")
                return False
        return False

    def obtener_todas_personas(self):
        con = self.conexion.obtener_conexion()
        personas = []
        if con is not None:
            try:
                query = "SELECT nombre FROM Personas"
                cursor = con.cursor()
                cursor.execute(query)
                for row in cursor.fetchall():
                    personas.append(row[0])
                con.close()
            except Exception as e:
                print(f"Error al obtener personas: {e}")
        return personas
