from Saves.SaveDict import save
from Controllers.TaskController import CreateTaskDict, UpdateTaskFields, MarkAsCompleted, ValidateTaskData

class TaskManager:
    """Handles the business logic for managing tasks."""
    
    def __init__(self):
        self.tasks = save

    def GetTask(self, task_id: int):
        """Returns a task by its ID."""
        if not isinstance(task_id, int):
            raise TypeError(f"ID must be int, got {type(task_id).__name__}")
        
        task = next((t for t in self.tasks if t['id'] == task_id), None)

        if task is None:
            raise ValueError(f"Task with ID {task_id} not found (out of range).")
        return task
    
    def AddTask(self, task: dict):
        """
        Adds a completed task (dict) to the list.
        If ID is not specified, generates it automatically.
        """
        ValidateTaskData(task)
        if 'id' not in task:
            if not self.tasks:
                task['id'] = 1
            else:
                task['id'] = max(t['id'] for t in self.tasks) + 1
        
        task.setdefault('priority', 'Medium')
        task.setdefault('completed', False)
        new_task = CreateTaskDict(task['description'], task['priority'], task['id'])
        
        self.tasks.append(new_task)
        return task

    def ChangeTask(self, task_id: int, nTask: dict):
        """
        Updates an existing task by ID with data from nTask.
        """
        ValidateTaskData(nTask)
        task = self.GetTask(task_id)
        if task:
            return UpdateTaskFields(task, nTask)
        return None

    def RemoveTask(self, task_id: int):
        """
        Deletes a task by its ID. Raises an error if the task is not found.
        """
        if not isinstance(task_id, int):
            raise TypeError("ID must be an integer")
            
        task = self.GetTask(task_id)
        self.tasks.remove(task)
        return True

    def CompleteTask(self, task_id):
        """
        Implementation of Ticket: User can select a task by ID and mark it complete.
        Searches for the task ID and updates the 'completed' field to True.
        """
        task = self.GetTask(task_id)
        if task:
            return MarkAsCompleted(task)
        return None

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self.tasks