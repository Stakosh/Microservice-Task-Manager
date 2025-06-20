"""
Repositorio en memoria para la gestión de tareas.

Este repositorio permite agregar, obtener y eliminar tareas almacenadas en una lista interna.
Ideal para pruebas o aplicaciones sin necesidad de persistencia en disco.
- Clase TaskRepoPersistent: gestiona la carga y almacenamiento persistente de tareas en un archivo JSON.
"""

from typing import List
from mvc.models.task import Task
import json
import os
TASKS_FILE = os.path.join(os.path.dirname(__file__), '../storage/tasks.json')


class TaskRepoInMemory:
    """
    Repositorio que maneja la persistencia en memoria de las tareas.
    """

    def __init__(self):
        """Inicializa el repositorio con una lista vacía de tareas."""
        self.tasks: List[Task] = []

    @staticmethod
    def load_tasks() -> List[Task]:
        """
        Simula la carga de tareas desde una fuente persistente (en este caso, en memoria).

        Retorna:
        - list[Task]: Lista de tareas (vacía por defecto).
        """
        return []

    @staticmethod
    def save_tasks(tasks: List[Task]):
        """
        Simula el guardado de tareas en una fuente persistente (en este caso, en memoria).

        Parámetros:
        - tasks (List[Task]): Lista de tareas a guardar.
        """
        print("Tareas guardadas en memoria.")

    def add_task(self, task: Task):
        """
        Agrega una nueva tarea al repositorio.

        Parámetros:
        - task (Task): La tarea que se desea agregar.
        """
        self.tasks.append(task)

    def get_all_tasks(self) -> List[Task]:
        """
        Retorna todas las tareas almacenadas.

        Retorna:
        - list[Task]: Lista de tareas.
        """
        return self.tasks

    def delete_task(self, index: int) -> bool:
        """
        Elimina una tarea según su índice.

        Parámetros:
        - index (int): Índice de la tarea a eliminar.

        Retorna:
        - bool: True si la tarea fue eliminada, False si el índice no es válido.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False


class TaskRepoPersistent:
    """
    Repositorio que maneja la persistencia de tareas en un archivo JSON.

    Métodos:
    - load_tasks(): retorna una lista de objetos Task desde el archivo.
    - save_tasks(tasks): guarda una lista de objetos Task en el archivo.
    """

    @staticmethod
    def load_tasks():
        """
        Carga las tareas desde el archivo JSON.

        Retorna:
        - list[Task]: Lista de tareas cargadas.
        """
        if not os.path.exists(TASKS_FILE):
            return []

        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def save_tasks(tasks):
        """
        Guarda las tareas en el archivo JSON.

        Parámetros:
        - tasks (list[Task]): Lista de objetos Task a guardar.
        """
        tasks_data = [task.to_dict() for task in tasks]
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)