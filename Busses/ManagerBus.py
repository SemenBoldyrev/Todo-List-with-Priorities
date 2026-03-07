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
        return new_task

    def complete_task(self, task_id):
        """
        Implementation of Ticket: User can select a task by ID and mark it complete.
        Searches for the task ID and updates the 'completed' field to True.
        """
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True #
                return task
        return None # Return None if ID is not found

    def get_tasks(self):
        """Returns the current list of tasks."""
        return self.tasks