from Saves.SaveDict import LoadData, SaveData


class TaskManager:
    """Handles the business logic for managing tasks."""

    def __init__(self):
        self.tasks = LoadData()

    def add_task(self, description, priority='Medium'):
        """
        Adds a new task to the task list.
        """
        if not self.tasks:
            new_id = 1
        else:
            new_id = max(task['id'] for task in self.tasks) + 1

        new_task = {
            'id': new_id,
            'description': description,
            'priority': priority,
            'completed': False
        }

        self.tasks.append(new_task)
        SaveData(self.tasks)
        return new_task

    def complete_task(self, task_id):
        """
        Marks a task as completed by ID.
        """
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                SaveData(self.tasks)
                return task
        return None

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self.tasks