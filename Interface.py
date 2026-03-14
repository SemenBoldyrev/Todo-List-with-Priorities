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

        printable_variants = []
        for item in variants:
            printable_variants.append(str(item))

        print("Choose an option:")
        for index, variant in enumerate(printable_variants):
            print(f"{index}: {variant}")

        user_input = input("Enter option: ")

        if user_input in printable_variants:
            return printable_variants.index(user_input)

        return -1

    except Exception:
        return -1