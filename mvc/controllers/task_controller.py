"""
Controlador que gestiona la interacción entre el modelo, la vista y el repositorio.

Esta clase es responsable de orquestar las operaciones del usuario final
con la lógica del sistema. Coordina las acciones solicitadas (agregar,
completar, eliminar y mostrar tareas), gestionando la comunicación entre
el modelo (Task), la vista (TaskView) y el repositorio.

A través de sus métodos, esta clase ofrece una interfaz de alto nivel
para manejar tareas en un sistema de gestión de tareas basado en el
patrón de arquitectura MVC.
"""

from mvc.views.task_view import TaskView
from mvc.models.task import Task


class TaskController:
    def __init__(self, repo, view=None):
        """
        Inicializa el controlador con una instancia del repositorio y la vista.
        Permite inyectar dependencias para facilitar pruebas.
        """
        self.repo = repo  # Se espera una instancia, no una clase
        self.view = view if view else TaskView()
        self.tasks = self.repo.load_tasks()

    def show_tasks(self):
        """Muestra todas las tareas disponibles."""
        self.view.show_tasks(self.tasks)

    def add_task(self):
        """Solicita al usuario una nueva tarea y la guarda."""
        title = self.view.get_task_input()
        if not title.strip():
            self.view.show_message("El título no puede estar vacío.")
            return
        new_task = Task(title)
        self.tasks.append(new_task)
        self.repo.save_tasks(self.tasks)
        self.view.show_message("Tarea agregada correctamente.")

    def complete_task(self):
        """Marca una tarea como completada según el número ingresado por el usuario."""
        self.view.show_tasks(self.tasks)
        try:
            task_number = self.view.get_task_number()
        except ValueError:
            self.view.show_message("Por favor, ingresa un número válido.")
            return

        task = self._get_task_by_number(task_number)
        if task:
            task.mark_completed()
            self.repo.save_tasks(self.tasks)
            self.view.show_message("Tarea completada.")
        else:
            self.view.show_message("Número de tarea inválido.")

    def delete_task(self):
        """Elimina una tarea según el número ingresado por el usuario."""
        self.view.show_tasks(self.tasks)
        try:
            task_number = self.view.get_task_number()
        except ValueError:
            self.view.show_message("Por favor, ingresa un número válido.")
            return

        task = self._get_task_by_number(task_number)
        if task:
            self.tasks.remove(task)
            self.repo.save_tasks(self.tasks)
            self.view.show_message("Tarea eliminada.")
        else:
            self.view.show_message("Número de tarea inválido.")

    def _get_task_by_number(self, number):
        """
        Devuelve la tarea correspondiente al número ingresado por el usuario.
        Si el número es inválido, retorna None.
        """
        if 0 < number <= len(self.tasks):
            return self.tasks[number - 1]
        return None