def CreateTask(desc: str, prior: str) -> dict:
    if type(desc) != str or type(prior) != str:
        raise ValueError("Description and priority must be strings.")
    return {
        "id": 0,
        "description": desc,
        "priority": prior,
        "completed": False
    }