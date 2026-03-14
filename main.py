from Busses.ManagerBus import TaskManager
from Saves.PriorityTypes import GetPriorityList
from Filter.Filter import FilterByCompletion, FilterByPriority

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
        print("5. Advanced Filter (Completion + Priority)")
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
            current_filtered_list = manager.get_tasks()

            print("\nStep 1: Filter by completion status")
            print("1. Completed only")
            print("2. In-progress only")
            print("3. Skip (Show both)")
            comp_choice = input("Select (1/2/3): ")
            
            if comp_choice == '1':
                current_filtered_list = FilterByCompletion(current_filtered_list, True)
            elif comp_choice == '2':
                current_filtered_list = FilterByCompletion(current_filtered_list, False)

            print("\nStep 2: Filter by priority")
            for idx, p in enumerate(priorities):
                print(f"{idx + 1}. {p}")
            print(f"{len(priorities) + 1}. Skip (Show all priorities)")
            
            p_choice = input(f"Select (1-{len(priorities) + 1}): ")
            
            try:
                p_idx = int(p_choice) - 1
                if 0 <= p_idx < len(priorities):
                    selected_priority = priorities[p_idx]
                    current_filtered_list = FilterByPriority(current_filtered_list, selected_priority)
            except ValueError:
                pass

            print("\n--- Filtered Results ---")
            display_tasks(current_filtered_list)

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()