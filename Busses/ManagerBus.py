from Saves.SaveDict import save

class TaskManager:
    """Handles the business logic for managing tasks."""
    
    def __init__(self):
        self.tasks = save

    def add_task(self, description, priority='Medium'):
        """
        Implementation of the ticket: Task is added to the task list.
        Generates a new ID and appends the task to the list.
        """
        new_id = max([task['id'] for task in self.tasks], default=0) + 1
        
        new_task = {
            'id': new_id,
            'description': description,
            'priority': priority,
            'completed': False
        }
        
        self.tasks.append(new_task)
        return new_task

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self.tasks