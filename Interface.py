def ShowMajorSeparation():
    print("=" * 40)


def ShowMinorSeparation():
    print("-" * 40)


def ShowText(text):
    print(text)


def ShowTaskList(data):
    if not data:
        print("No relevant tasks found")
        return

    for task in data:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] ID:{task['id']} - {task['description']} ({task['priority']})")


def ShowChoice(variants: list) -> int:
    print("Choose an option:")

    for index, variant in enumerate(variants, start=1):
        print(f"{index}. {variant}")

    choice = int(input("Enter choice number: "))
    return choice