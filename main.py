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


    print("\n" + "="*30)
    print("\nCurrent Task List:")
    for task in manager.get_tasks():
        status = "Done" if task['completed'] else "Pending"
        print(f"[{task['id']}] {task['description']} - Priority: {task['priority']} ({status})")
    print("\n" + "="*30)

if __name__ == "__main__":
    main()