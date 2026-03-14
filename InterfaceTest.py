from Interface import (
    ShowMajorSeparation,
    ShowMinorSeparation,
    ShowText,
    ShowTaskList,
    ShowChoice
)


def run_display_tests():
    print("TEST 1: ShowMajorSeparation")
    ShowMajorSeparation()

    print("\nTEST 2: ShowMinorSeparation")
    ShowMinorSeparation()

    print("\nTEST 3: ShowText")
    ShowText("Hello from ShowText")

    print("\nTEST 4: ShowTaskList with valid data")
    test_tasks = [
        {
            "id": 1,
            "description": "Complete homework",
            "priority": "High",
            "completed": False
        },
        {
            "id": 2,
            "description": "Read a book",
            "priority": "Medium",
            "completed": True
        }
    ]
    ShowTaskList(test_tasks)

    print("\nTEST 5: ShowTaskList with empty list")
    ShowTaskList([])


def run_choice_tests():
    print("\nTEST 6: ShowChoice with strings")
    result = ShowChoice(["resume", "exit"])
    print("Result:", result)

    print("\nTEST 7: ShowChoice with numbers")
    result = ShowChoice([1, 2, 3])
    print("Result:", result)

    print("\nTEST 8: ShowChoice with mixed data")
    result = ShowChoice(["resume", 123, True])
    print("Result:", result)


if __name__ == "__main__":
    run_display_tests()
    run_choice_tests()