from Busses.ManagerBus import TaskManager

def main():
    manager = TaskManager()

    print("--- Todo List Manager ---")
    
    description = input("Enter task description: ")

    new_task = manager.add_task(description)
    
    print(f"\nSuccessfully added task: '{new_task['description']}'")

    print("\nCurrent Task List:")
    for task in manager.get_tasks():
        status = "Done" if task['completed'] else "Pending"
        print(f"[{task['id']}] {task['description']} - Priority: {task['priority']} ({status})")

if __name__ == "__main__":
    main()