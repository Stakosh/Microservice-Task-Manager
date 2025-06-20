"""
Punto de entrada de la aplicación.

Este archivo orquesta la ejecución de la lógica principal:
    1. Muestra el menú de opciones al usuario.
    2. Lee la opción seleccionada.
    3. Ejecuta la acción correspondiente (agregar, listar, completar, eliminar o salir).
    4. Mantiene un ciclo continuo de interacción hasta que el usuario decide salir.
"""

from mvc.controllers.task_controller import TaskController
from mvc.storage.task_repo import TaskRepoPersistent

def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n=== Menú Principal ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    """
    Función principal que inicializa el controlador y gestiona la interacción con el usuario.
    """
    repo = TaskRepoPersistent()
    controller = TaskController(repo=repo)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        acciones = {
            "1": controller.show_tasks,
            "2": controller.add_task,
            "3": controller.complete_task,
            "4": controller.delete_task
        }

        if opcion in acciones:
            acciones[opcion]()  # Ejecuta la acción correspondiente
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")

if __name__ == "__main__":
    main()