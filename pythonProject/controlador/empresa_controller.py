from dao.persona_dao import PersonaDAO
class EmpresaController:
    def __init__(self):
        self.persona_dao = PersonaDAO()

    def agregar_persona(self, nombre):
        return self.persona_dao.agregar_persona(nombre)

    def eliminar_persona(self, nombre):
        return self.persona_dao.eliminar_persona(nombre)

    def mostrar_personas(self):
        return self.persona_dao.obtener_todas_personas()
