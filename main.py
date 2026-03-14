from Busses.ManagerBus import TaskManager
from Saves.PriorityTypes import GetPriorityList

def main():
    manager = TaskManager()
    priorities = GetPriorityList()

    print("--- Todo List Manager ---")
    
    description = input("Enter task description: ")
    print(f"Available priorities: {', '.join(priorities)}")
    priority = input(f"Choose priority (default 'Medium'): ")

    if priority not in priorities:
        priority = "Medium"

    task_data = {
        'description': description,
        'priority': priority
    }
    new_task = manager.AddTask(task_data)
    
    print("\n" + "="*30)
    print(f"SUCCESS: Task created successfully!")
    print(f"ID: {new_task['id']}")
    print(f"Description: {new_task['description']}")
    print(f"Priority: {new_task['priority']}")
    print("="*30)


    print("\n--- Current Task List ---")
    for t in manager.get_tasks():
        status = "✓" if t['completed'] else " " 
        print(f"[{status}] ID: {t['id']} [{t['priority']}] - {t['description']}")
    print("="*30)

    try:
        target_id = int(input("\nEnter the ID of the task to mark complete: "))
        
        task_to_update = manager.GetTask(target_id)

        if task_to_update:
            manager.ChangeTask(target_id, {'completed': True})
            print(f"\nSUCCESS: Task {target_id} marked as complete!")
        else:
            print(f"\nERROR: Task with ID {target_id} not found.")
            
    except ValueError:
        print("\nERROR: Please enter a valid numeric ID.")

    print("\n--- Updated Task List ---")
    for t in manager.get_tasks():
        status = "✓" if t['completed'] else " " 
        print(f"[{status}] ID: {t['id']} - {t['description']}")

if __name__ == "__main__":
    main()