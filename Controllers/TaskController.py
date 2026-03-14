def ValidateTaskData(task: dict):
    """Checks that task is a dictionary and contains required string fields."""
    if not isinstance(task, dict):
        raise TypeError(f"Expected dict, got {type(task).__name__}")

    if "description" in task and not isinstance(task["description"], str):
        raise TypeError("Description must be a string")

    if "priority" in task and not isinstance(task["priority"], str):
        raise TypeError("Priority must be a string")

    if "completed" in task and not isinstance(task["completed"], bool):
        raise TypeError("Completed must be a boolean")


def CreateTaskDict(description: str, priority: str = "Medium", task_id: int = None) -> dict:
    """
    Creates a task dictionary with the given description, priority, and optional ID.
    If ID is not provided, it will be generated when the task is added to the manager.
    """
    if not isinstance(description, str):
        raise TypeError("Description must be a string")

    if not isinstance(priority, str):
        raise TypeError("Priority must be a string")

    task = {
        "description": description,
        "priority": priority,
        "completed": False
    }

    if task_id is not None:
        if not isinstance(task_id, int):
            raise TypeError("ID must be an integer")
        task["id"] = task_id

    return task


def UpdateTaskFields(task: dict, updates: dict) -> dict:
    """
    Updates the fields of a task with the provided updates.
    Only allows updating description, priority, and completed status.
    """
    if not isinstance(task, dict):
        raise TypeError("Task must be a dictionary")

    if not isinstance(updates, dict):
        raise TypeError("Updates must be a dictionary")

    ValidateTaskData(updates)

    allowed_fields = {"description", "priority", "completed"}
    clean_updates = {key: value for key, value in updates.items() if key in allowed_fields}

    task.update(clean_updates)
    return task


def MarkAsCompleted(task: dict) -> dict:
    """
    Marks a task as completed by setting its 'completed' field to True.
    """
    if not isinstance(task, dict):
        raise TypeError("Task must be a dictionary")

    task["completed"] = True
    return task


def RemoveTask(tasks: list, task_id: int) -> dict:
    """
    Removes a task from the task list by ID and returns the removed task.

    Raises:
        TypeError: if task_id is not an integer or tasks is not a list.
        ValueError: if task with the given ID is not found.
    """
    if not isinstance(tasks, list):
        raise TypeError("Tasks must be a list")

    if not isinstance(task_id, int):
        raise TypeError("ID must be an integer")

    for index, task in enumerate(tasks):
        if task.get("id") == task_id:
            return tasks.pop(index)

    raise ValueError(f"Task with ID {task_id} not found (out of range).")