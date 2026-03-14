from Busses.ManagerBus import TaskManager
from Saves.PriorityTypes import GetPriorityList
from Filter.Filter import FilterByCompletion

def display_tasks(tasks):
    """Helps display tasks in a formatted table."""
    print("\n" + "="*100)
    print(f"{'ID':<4} | {'Status':<8} | {'Priority':<8} | {'Description'}")
    print("-" * 100)
    for t in tasks:
        status = "[✓]" if t['completed'] else "[ ]"
        print(f"{t['id']:<4} | {status:<8} | {t['priority']:<8} | {t['description']}")
    print("="*100 + "\n")

def main():
    manager = TaskManager()
    priorities = GetPriorityList()

    while True:
        print("--- Todo List Manager ---")
        print("1. Show all tasks")
        print("2. Add new task")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Filter by completion")
        print("6. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            tasks = manager.get_tasks()
            if not tasks:
                print("\nYour todo list is empty.")
            else:
                display_tasks(tasks)

        elif choice == '2':
            description = input("Enter task description: ")
            print(f"Available priorities: {', '.join(priorities)}")
            priority = input("Choose priority (default 'Medium'): ")
            if priority not in priorities:
                priority = "Medium"
            
            manager.AddTask({'description': description, 'priority': priority})
            print("\nSUCCESS: Task added!")

        elif choice == '3':
            try:
                target_id = int(input("\nEnter task ID to complete: "))
                if manager.ChangeTask(target_id, {'completed': True}):
                    print(f"Task {target_id} updated!")
                else:
                    print("Error: Task not found.")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                target_id = int(input("\nEnter task ID to remove: "))
                confirm = input(f"Are you sure you want to delete task {target_id}? (y/n): ")
                if confirm.lower() == 'y':
                    manager.RemoveTask(target_id)
                    print(f"SUCCESS: Task {target_id} has been removed.")
                else:
                    print("Deletion cancelled.")
            except (ValueError, TypeError) as e:
                print(f"ERROR: {e}")

        elif choice == '5':
            print("\nFilter by:")
            print("1. Completed tasks")
            print("2. In-progress tasks")
            filter_choice = input("Select (1/2): ")
            
            all_tasks = manager.get_tasks()
            try:
                if filter_choice == '1':
                    filtered = FilterByCompletion(all_tasks, True)
                    print("\n--- Completed Tasks ---")
                    display_tasks(filtered)
                elif filter_choice == '2':
                    filtered = FilterByCompletion(all_tasks, False)
                    print("\n--- In-Progress Tasks ---")
                    display_tasks(filtered)
                else:
                    print("Invalid filter selection.")
            except ValueError as e:
                print(f"Filter Error: {e}")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()