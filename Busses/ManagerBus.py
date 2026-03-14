from Saves.SaveDict import save
from Controllers.TaskController import (
    CreateTaskDict,
    UpdateTaskFields,
    MarkAsCompleted,
    ValidateTaskData,
    RemoveTask as RemoveTaskFromList
)


class TaskManager:
    """Handles the business logic for managing tasks."""

    def __init__(self):
        # Create a copy so tests and runtime do not mutate the original save directly
        self.tasks = [dict(task) for task in save]

    def GetTask(self, task_id: int):
        """Returns a task by its ID."""
        if not isinstance(task_id, int):
            raise TypeError(f"ID must be int, got {type(task_id).__name__}")

        task = next((t for t in self.tasks if t["id"] == task_id), None)

        if task is None:
            raise ValueError(f"Task with ID {task_id} not found (out of range).")

        return task

    def AddTask(self, task: dict):
        """
        Adds a task (dict) to the list.
        If ID is not specified, generates it automatically.
        """
        ValidateTaskData(task)

        if "description" not in task:
            raise ValueError("Task must contain description")

        if "id" not in task:
            if not self.tasks:
                task["id"] = 1
            else:
                task["id"] = max(t["id"] for t in self.tasks) + 1

        task.setdefault("priority", "Medium")
        task.setdefault("completed", False)

        new_task = CreateTaskDict(task["description"], task["priority"], task["id"])
        new_task["completed"] = task["completed"]

        self.tasks.append(new_task)
        return new_task

    def ChangeTask(self, task_id: int, nTask: dict):
        """
        Updates an existing task by ID with data from nTask.
        """
        ValidateTaskData(nTask)
        task = self.GetTask(task_id)
        return UpdateTaskFields(task, nTask)

    def RemoveTask(self, task_id: int):
        """
        Deletes a task by its ID.
        Returns True if deletion was successful.
        """
        RemoveTaskFromList(self.tasks, task_id)
        return True

    def CompleteTask(self, task_id: int):
        """
        Marks a task complete by ID.
        """
        task = self.GetTask(task_id)
        return MarkAsCompleted(task)

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self.tasks