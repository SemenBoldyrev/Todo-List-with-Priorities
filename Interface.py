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
    try:
        if not variants:
            return -1

        for item in variants:
            str(item)

        print("Choose an option:")
        for index, variant in enumerate(variants):
            print(f"{index}: {variant}")

        user_input = input("Enter option: ")

        if user_input not in variants:
            return -1

        return variants.index(user_input)

    except Exception:
        return -1