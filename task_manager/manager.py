from models import Task
from storage import load_raw_tasks,save_raw_task
from typing import List

class TaskManager:
    def __init__(self):
        self._load_all_tasks()

    def _load_all_tasks(self) -> None:
        """Internal helper to convert raw storage dictionaries into active OOP Task objects"""
        raw_list = load_raw_tasks()
        self.tasks: List[Task] = [Task.from_dict(item) for item in raw_list]
    def _save_all_task(self) -> None:
        """Internal helper to convert objects back to dictionary format and commit changes."""
        raw_list = [task.to_dict() for task in self.tasks]
        save_raw_task(raw_list)

    def add_task(self, description: str) -> int:
        """Validates input, assigns a unique ID, and creates a task""" 
        if not description.strip():
            raise ValueError("Task description cannot be empty or whitespace.")
        next_id = max([task.id for task in self.tasks]) + 1 if self.tasks else 1

        new_task = Task(task_id=next_id, description=description)
        self.tasks.append(new_task)
        self._save_all_task()
        return next_id
    