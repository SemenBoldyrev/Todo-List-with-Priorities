from Busses.ManagerBus import TaskManager
from Interface import ShowMajorSeparation, ShowMinorSeparation, ShowText, ShowTaskList


def main():
    manager = TaskManager()

    ShowMajorSeparation()
    ShowText("--- Todo List Manager ---")
    ShowMajorSeparation()
    
    description = input("Enter task description: ")
    new_task = manager.add_task(description)
    
    print()
    ShowMajorSeparation()
    ShowText("SUCCESS: Task created successfully!")
    ShowText(f"ID: {new_task['id']}")
    ShowText(f"Description: {new_task['description']}")
    ShowMajorSeparation()

    print("\n--- Current Task List ---")
    ShowTaskList(manager.tasks)
    ShowMajorSeparation()

    try:
        target_id = int(input("\nEnter the ID of the task to mark complete: "))
        updated_task = manager.complete_task(target_id)

        if updated_task:
            ShowText(f"\nSUCCESS: Task {target_id} marked as complete!")
        else:
            ShowText(f"\nERROR: Task with ID {target_id} not found.")
            
    except ValueError:
        ShowText("\nERROR: Please enter a valid numeric ID.")

    print("\n--- Updated Task List ---")
    ShowTaskList(manager.tasks)


if __name__ == "__main__":
    main()