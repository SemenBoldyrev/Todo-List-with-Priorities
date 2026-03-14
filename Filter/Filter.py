def FilterByPriority(tasks: list, prior: str) -> list:
    if type(tasks) != list or type(prior) != str:
        raise ValueError("Tasks must be a list and priority must be a string.")
    nList = []
    for task in tasks:
        if task['priority'] == prior:
            nList.append(task)
    return nList

def FilterByCompletion(tasks: list, completion: bool) -> list:
    if type(tasks) != list or type(completion) != bool:
        raise ValueError("Tasks must be a list and completion must be a boolean.")
    nList = []
    for task in tasks:
        if task['completed'] == completion:
            nList.append(task)
    return nList