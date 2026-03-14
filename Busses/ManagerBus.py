from Saves.SaveDict import save
from Saves.PriorityTypes import GetPriorityList

class TaskManager:
    """Handles the business logic for managing tasks."""
    
    def __init__(self):
        self.tasks = save

    def GetTask(self, task_id: int):
        """Returns a task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def AddTask(self, task: dict):
        """
        Adds a completed task (dict) to the list.
        If ID is not specified, generates it automatically.
        """
        if 'id' not in task:
            if not self.tasks:
                task['id'] = 1
            else:
                task['id'] = max(t['id'] for t in self.tasks) + 1
        
        task.setdefault('priority', 'Medium')
        task.setdefault('completed', False)
        
        self.tasks.append(task)
        return task

    def ChangeTask(self, task_id: int, nTask: dict):
        """
        Updates an existing task by ID with data from nTask.
        """
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                nTask['id'] = task_id 
                self.tasks[i].update(nTask)
                return self.tasks[i]
        return None

    def add_task(self, description, priority='Medium'):
        """
        Implementation of the ticket: Task is added to the task list.
        Generates a new ID and appends the task to the list.
        """
        valid_priorities = GetPriorityList()
        if priority not in valid_priorities:
            priority = 'Medium'
        
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