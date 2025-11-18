import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import pytest
from datetime import date
from task_manager.manager import TaskManager, TaskExistsError, TaskNotFoundError, InvalidTaskError
from task_manager.models import Task

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task_success(manager):
    t = Task(id="1", title="Comprar leite")
    manager.add_task(t)
    assert manager.get_task("1").title == "Comprar leite"

def test_add_task_missing_fields_raises(manager):
    with pytest.raises(InvalidTaskError):
        manager.add_task(Task(id="", title=""))

def test_add_duplicate_task_raises(manager):
    manager.add_task(Task(id="1", title="A"))
    with pytest.raises(TaskExistsError):
        manager.add_task(Task(id="1", title="B"))

def test_remove_task_success(manager):
    manager.add_task(Task(id="1", title="Tarefa"))
    manager.remove_task("1")
    with pytest.raises(TaskNotFoundError):
        manager.get_task("1")

def test_remove_nonexistent_raises(manager):
    with pytest.raises(TaskNotFoundError):
        manager.remove_task("nope")

def test_complete_task_marks_completed(manager):
    manager.add_task(Task(id="2", title="Pagar conta"))
    manager.complete_task("2")
    assert manager.get_task("2").completed is True

def test_list_pending_and_completed(manager):
    manager.add_task(Task(id="a", title="A"))
    manager.add_task(Task(id="b", title="B"))
    manager.complete_task("b")
    pending = manager.list_pending()
    completed = manager.list_completed()
    assert len(pending) == 1 and pending[0].id == "a"
    assert len(completed) == 1 and completed[0].id == "b"

def test_edit_task_success_and_validation(manager):
    manager.add_task(Task(id="x", title="Old"))
    manager.edit_task("x", title="New", description="desc")
    assert manager.get_task("x").title == "New"
    with pytest.raises(InvalidTaskError):
        manager.edit_task("x", title="")

def test_due_date_type_validation(manager):
    manager.add_task(Task(id="d1", title="with due"))
    with pytest.raises(InvalidTaskError):
        manager.edit_task("d1", due_date="2025-01-01")

def test_get_nonexistent_raises(manager):
    with pytest.raises(TaskNotFoundError):
        manager.get_task("missing")
