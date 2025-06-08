'''
Este archivo se crea con la finalidad de
'''

import json
import os

# Definimos la ruta del archivo 'tasks.json' dentro de la carpeta monolitic
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

def load_tasks():
    """
    Carga las tareas desde el archivo JSON. Si el archivo no existe o tiene un formato incorrecto, retorna una lista vacía.
    Filtra las tareas que no contienen el campo 'title' y asegura que todas tengan 'completed'.
    """
    if not os.path.exists(TASKS_FILE):
        return []  # Si no existe el archivo, retornamos una lista vacía

    with open(TASKS_FILE, "r") as file:
        try:
            tasks = json.load(file)  # Cargamos las tareas desde el archivo
            valid_tasks = []
            for task in tasks:
                if isinstance(task, dict) and 'title' in task:
                    if 'completed' not in task:
                        task['completed'] = False  # Si no tiene 'completed', lo agregamos como False
                    valid_tasks.append(task)
            return valid_tasks
        except json.JSONDecodeError:
            return []  # Si hay un error al decodificar, retornamos una lista vacía

def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Guardamos las tareas con una indentación para legibilidad

def view_tasks(tasks):
    """
    Muestra todas las tareas en consola, indicando si están completadas o no.
    """
    # Códigos ANSI para colores
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    if not tasks:
        print("No hay tareas para mostrar.")
    else:
        print("\n=== Lista de Tareas ===")
        for idx, task in enumerate(tasks, start=1):
            #status = "✔" if task['completed'] else "✘"
            status = f"{GREEN}✔{RESET}" if task['completed'] else f"{RED}✘{RESET}"
            print(f"{idx}. {task['title']} {status}")

def add_task(tasks):
    """
    Agrega una nueva tarea a la lista de tareas.
    """
    title = input("Ingrese el título de la tarea: ")
    new_task = {'title': title, 'completed': False}  # Creamos la nueva tarea con título y estado 'completado' False
    tasks.append(new_task)
    save_tasks(tasks)  # Guardamos las tareas actualizadas

def complete_task(tasks):
    """
    Marca una tarea como completada.
    """
    view_tasks(tasks)  # Mostramos las tareas actuales
    task_number = int(input("Ingrese el número de la tarea a completar: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True  # Marcamos la tarea seleccionada como completada
        save_tasks(tasks)  # Guardamos las tareas actualizadas
        print("Tarea completada.")
    else:
        print("Número de tarea inválido.")

def delete_task(tasks):
    """
    Elimina una tarea de la lista de tareas.
    """
    view_tasks(tasks)  # Mostramos las tareas actuales
    task_number = int(input("Ingrese el número de la tarea a eliminar: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)  # Eliminamos la tarea seleccionada
        save_tasks(tasks)  # Guardamos las tareas actualizadas
        print("Tarea eliminada.")
    else:
        print("Número de tarea inválido.")

def main():
    """
    Función principal que gestiona el menú y la interacción con el usuario.
    """
    tasks = load_tasks()  # Cargamos las tareas al iniciar

    while True:
        print("\n=== Lista de Tareas ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            view_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()