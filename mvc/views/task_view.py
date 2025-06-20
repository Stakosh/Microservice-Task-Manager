"""
Vista encargada de interactuar con el usuario.

Provee métodos para mostrar tareas, obtener entradas y mostrar mensajes,
sin contener lógica de negocio ni manipulación directa de datos.
"""

class TaskView:
    """
    Vista que presenta información al usuario y recoge entradas.
    """

    @staticmethod
    def show_tasks(tasks):
        """
        Muestra la lista de tareas con su estado.

        Parámetros:
        - tasks (list): Lista de objetos Task.
        """
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"
        if not tasks:
            print("No hay tareas para mostrar.")
        else:
            print("\n=== Lista de Tareas ===")
            for idx, task in enumerate(tasks, start=1):
                status = f"{GREEN}✔{RESET}" if task.completed else f"{RED}✘{RESET}"
                print(f"{idx}. {task.title} {status}")

    @staticmethod
    def get_task_input():
        """
        Solicita al usuario el título de una nueva tarea.

        Retorna:
        - str: Título de la tarea ingresado por el usuario.
        """
        return input("Ingrese el título de la tarea: ")

    @staticmethod
    def get_task_number():
        """
        Solicita al usuario el número de una tarea.

        Retorna:
        - int: Número de tarea ingresado, o lanza ValueError si no es válido.
        """
        user_input = input("Ingrese el número de la tarea: ")
        number = int(user_input)  # Puede lanzar ValueError que será capturado desde el controlador
        return number

    @staticmethod
    def show_message(message):
        """
        Muestra un mensaje al usuario.

        Parámetros:
        - message (str): Mensaje a mostrar.
        """
        print(message)