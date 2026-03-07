from Busses.ManagerBus import TaskManager

def main():
    manager = TaskManager()

    print("--- Todo List Manager ---")
    
    print("Adding a new task...")
    manager.add_task("Review pull requests", priority="High")
    manager.add_task("Update documentation", priority="Low")

    print("\nCurrent Task List:")
    for task in manager.get_tasks():
        status = "Done" if task['completed'] else "Pending"
        print(f"[{task['id']}] {task['description']} - Priority: {task['priority']} ({status})")

if __name__ == "__main__":
    main()