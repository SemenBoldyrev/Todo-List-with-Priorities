def CreateTaskDict(description: str, priority: str = "Medium", task_id: int = None) -> dict:
    """
    Creates a task dictionary with the given description, priority, and optional ID.
    If ID is not provided, it will be generated when the task is added to the manager
    """
    task = {
        'description': description,
        'priority': priority,
        'completed': False
    }
    if task_id is not None:
        task['id'] = task_id
    return task

def UpdateTaskFields(task: dict, updates: dict) -> dict:
    """
    Updates the fields of a task with the provided updates.
    Only allows updating description, priority, and completed status.
    """
    updates.pop('id', None)
    task.update(updates)
    return task

def MarkAsCompleted(task: dict) -> dict:
    """
    Marks a task as completed by setting its 'completed' field to True.
    """
    task['completed'] = True
    return task