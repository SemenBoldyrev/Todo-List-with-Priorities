from Busses.ManagerBus import TaskManager
from Saves.SaveDict import save


def reset_data():
    save.clear()
    save.extend([
        {
            'id': 1,
            'description': 'Complete project proposal',
            'priority': 'High',
            'completed': False
        },
        {
            'id': 2,
            'description': 'Read documentation',
            'priority': 'Medium',
            'completed': False
        }
    ])


def run_tests():
    print("TEST 1: Remove existing task")
    reset_data()
    manager = TaskManager()

    result = manager.RemoveTask(1)
    print("Expected: True")
    print("Actual:", result)
    print("Tasks left:", manager.get_tasks())

    print("\nTEST 2: Remove non-existing task")
    reset_data()
    manager = TaskManager()

    result = manager.RemoveTask(99)
    print("Expected: False")
    print("Actual:", result)
    print("Tasks left:", manager.get_tasks())

    print("\nTEST 3: Remove with invalid ID type")
    reset_data()
    manager = TaskManager()

    try:
        manager.RemoveTask("abc")
    except Exception as e:
        print("Expected: TypeError")
        print("Actual:", type(e).__name__, "-", e)


if __name__ == "__main__":
    run_tests()