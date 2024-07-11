import tkinter as tk
from tkinter import messagebox
from controlador.empresa_controller import EmpresaController

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empresa")

        self.empresa_controller = EmpresaController()

        # Crear widgets
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.entry_nombre = tk.Entry(root, width=30)
        self.btn_agregar = tk.Button(root, text="Agregar Persona", command=self.agregar_persona)
        self.btn_eliminar = tk.Button(root, text="Eliminar Persona", command=self.eliminar_persona)
        self.btn_mostrar = tk.Button(root, text="Mostrar Personas", command=self.mostrar_personas)
        self.lista_personas = tk.Listbox(root, width=50)

        # Ubicar widgets en la interfaz
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.btn_agregar.grid(row=1, column=0, padx=10, pady=10)
        self.btn_eliminar.grid(row=1, column=1, padx=10, pady=10)
        self.btn_mostrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.lista_personas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def agregar_persona(self):
        nombre = self.entry_nombre.get()
        if nombre:
            if self.empresa_controller.agregar_persona(nombre):
                messagebox.showinfo("Éxito", f"Persona '{nombre}' agregada exitosamente.")
                self.entry_nombre.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al agregar persona.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un nombre.")

    def eliminar_persona(self):
        nombre = self.entry_nombre.get()
        if nombre:
            if self.empresa_controller.eliminar_persona(nombre):
                messagebox.showinfo("Éxito", f"Persona '{nombre}' eliminada exitosamente.")
                self.entry_nombre.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al eliminar persona.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un nombre.")

    def mostrar_personas(self):
        self.lista_personas.delete(0, tk.END)  # Limpiar lista actual
        personas = self.empresa_controller.mostrar_personas()
        for persona in personas:
            self.lista_personas.insert(tk.END, persona)

def iniciar_interfaz():
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
