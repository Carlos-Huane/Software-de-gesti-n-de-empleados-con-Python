from controlador.empresa_controller import EmpresaController
from vista.interfaz import Interfaz

empresa_controller = EmpresaController()
interfaz = Interfaz()

opcion = 1
while opcion != 4:
    interfaz.mostrar_menu()
    opcion = int(input("¿Qué opción desea elegir?: "))
    if opcion == 1:
        nombre_persona = interfaz.solicitar_datos_persona()
        if empresa_controller.agregar_persona(nombre_persona):
            print("Persona agregada exitosamente.")
        else:
            print("Error al agregar persona.")
    elif opcion == 2:
        personas = empresa_controller.mostrar_personas()
        interfaz.mostrar_personas(personas)
    elif opcion == 3:
        nombre_persona = interfaz.solicitar_datos_persona()
        if empresa_controller.eliminar_persona(nombre_persona):
            print("Persona eliminada exitosamente.")
        else:
            print("Error al eliminar persona.")
    elif opcion == 4:
        print("Gracias por utilizar la aplicación de la empresa. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente de nuevo.")
