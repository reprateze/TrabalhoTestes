from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    id: str
    title: str
    description: str = None
    due_date: date = None
    completed: bool = False
