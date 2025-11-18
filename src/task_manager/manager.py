from datetime import date
from .models import Task

# ----- EXCEÇÕES PERSONALIZADAS -----
class TaskError(Exception):
    pass

class TaskExistsError(TaskError):
    pass

class TaskNotFoundError(TaskError):
    pass

class InvalidTaskError(TaskError):
    pass


# ----- GERENCIADOR DE TAREFAS -----
class TaskManager:
    def __init__(self):
        self.tasks = {}

    # ----- ADICIONAR -----
    def add_task(self, task: Task):
        if not task.id or not task.title:
            raise InvalidTaskError("ID e título são obrigatórios.")

        if task.id in self.tasks:
            raise TaskExistsError("Tarefa já existe.")

        self.tasks[task.id] = task

    # ----- OBTER -----
    def get_task(self, task_id: str) -> Task:
        if task_id not in self.tasks:
            raise TaskNotFoundError("Tarefa não encontrada.")
        return self.tasks[task_id]


    # ----- REMOVER -----
    def remove_task(self, task_id: str):
        if task_id not in self.tasks:
            raise TaskNotFoundError("Tarefa não encontrada.")
        del self.tasks[task_id]

    # ----- MARCAR COMO CONCLUÍDA -----
    def complete_task(self, task_id: str):
        task = self.get_task(task_id)
        task.completed = True

    # ----- EDITAR -----
    def edit_task(self, task_id: str, title=None, description=None, due_date=None):
        task = self.get_task(task_id)

        if title is not None:
            if title == "":
                raise InvalidTaskError("Título inválido.")
            task.title = title
        
        if description is not None:
            task.description = description

        if due_date is not None:
            if not isinstance(due_date, date):
                raise InvalidTaskError("due_date deve ser datetime.date")
            task.due_date = due_date

    # ----- LISTAR -----
    def list_all(self):
        return list(self.tasks.values())

    def list_pending(self):
        return [t for t in self.tasks.values() if not t.completed]

    def list_completed(self):
        return [t for t in self.tasks.values() if t.completed]
