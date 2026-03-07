from Busses.ManagerBus import TaskManager

def main():
    manager = TaskManager()

    print("--- Todo List Manager ---")
    
    description = input("Enter task description: ")
    new_task = manager.add_task(description)
    
    print("\n" + "="*30)
    print(f"SUCCESS: Task created successfully!")
    print(f"ID: {new_task['id']}")
    print(f"Description: {new_task['description']}")
    print("="*30)


    print("\n--- Current Task List ---")
    for t in manager.tasks:
        status = "✓" if t['completed'] else " " 
        print(f"[{status}] ID: {t['id']} - {t['description']}")
    print("="*30)

    try:
        target_id = int(input("\nEnter the ID of the task to mark complete: "))
        updated_task = manager.complete_task(target_id) #

        if updated_task:
            print(f"\nSUCCESS: Task {target_id} marked as complete!")
        else:
            print(f"\nERROR: Task with ID {target_id} not found.")
            
    except ValueError:
        print("\nERROR: Please enter a valid numeric ID.")

    print("\n--- Updated Task List ---")
    for t in manager.tasks:
        status = "✓" if t['completed'] else " " 
        print(f"[{status}] ID: {t['id']} - {t['description']}")

if __name__ == "__main__":
    main()