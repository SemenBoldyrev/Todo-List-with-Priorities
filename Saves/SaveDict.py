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

if __name__ == "__main__":
    test_data = [
        {
            "id": 2,
            "description": "Test task",
            "priority": "Medium",
            "completed": False
        }
    ]

    save_result = SaveData(test_data)
    loaded_data = LoadData()

    print("Save result:", save_result)
    print("Loaded data:", loaded_data)