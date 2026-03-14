from Interface import ShowMajorSeparation, ShowMinorSeparation, ShowText, ShowTaskList


def run_tests():
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


if __name__ == "__main__":
    run_tests()