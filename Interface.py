def ShowMajorSeparation():
    print("=" * 40)


def ShowMinorSeparation():
    print("-" * 40)


def ShowText(text):
    print(text)


def ShowTaskList(data):
    for task in data:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] ID:{task['id']} - {task['description']} ({task['priority']})")