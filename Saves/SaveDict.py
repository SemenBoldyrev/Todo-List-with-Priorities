data_holder = [
    {
        "id": 1,
        "description": "Complete project proposal",
        "priority": "High",
        "completed": False
    }
]


def SaveData(data: list):
    """Saves task data into temporary storage."""
    global data_holder

    if not isinstance(data, list):
        return False

    data_holder = data
    return True


def LoadData() -> list:
    """Loads task data from temporary storage."""
    return data_holder