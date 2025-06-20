"""
Modelo de datos y repositorio para la gestión de tareas.

Contiene:
- Clase Task: representa una tarea individual.
"""

class Task:
    """
    Representa una tarea con título y estado de completado.

    Atributos:
    - title (str): Título de la tarea.
    - completed (bool): Estado de completado de la tarea (por defecto: False).
    """
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_completed(self):
        """Marca la tarea como completada."""
        self.completed = True

    def to_dict(self):
        """
        Convierte la tarea en un diccionario.

        Retorna:
        - dict: representación de la tarea.
        """
        return {
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """
        Crea una instancia de Task desde un diccionario.

        Parámetros:
        - data (dict): Diccionario con las claves 'title' y 'completed'.

        Retorna:
        - Task: instancia de tarea.
        """
        return Task(
            title=data.get('title', ''),
            completed=data.get('completed', False)
        )