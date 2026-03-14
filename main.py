from Busses.ManagerBus import TaskManager
from Saves.PriorityTypes import GetPriorityList
from Filter.Filter import FilterByCompletion, FilterByPriority


def display_tasks(tasks, empty_message="No tasks found."):
    """Helps display tasks in a formatted table with a custom empty message."""
    if not tasks:
        print(f"\n{empty_message}")
        return

    print("\n" + "=" * 100)
    print(f"{'ID':<4} | {'Status':<8} | {'Priority':<8} | {'Description'}")
    print("-" * 100)

    for task in tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{task['id']:<4} | {status:<8} | {task['priority']:<8} | {task['description']}")

    print("=" * 100 + "\n")


def main():
    manager = TaskManager()
    priorities = GetPriorityList()

    while True:
        print("--- Todo List Manager ---")
        print("1. Show all tasks")
        print("2. Add new task")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Filter by priority")
        print("6. Advanced Filter (Completion + Priority)")
        print("7. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            tasks = manager.get_tasks()
            if not tasks:
                print("\nYour todo list is empty.")
            else:
                display_tasks(tasks)

        elif choice == "2":
            description = input("Enter task description: ").strip()
            if not description:
                print("ERROR: Description cannot be empty.")
                continue

            print(f"Available priorities: {', '.join(priorities)}")
            priority = input("Choose priority (default 'Medium'): ").strip()

            if priority not in priorities:
                priority = "Medium"

            manager.AddTask({
                "description": description,
                "priority": priority
            })
            print("\nSUCCESS: Task added!")

        elif choice == "3":
            try:
                target_id = int(input("\nEnter task ID to complete: "))
                manager.ChangeTask(target_id, {"completed": True})
                print(f"SUCCESS: Task {target_id} updated!")
            except (ValueError, TypeError) as error:
                print(f"ERROR: {error}")

        elif choice == "4":
            try:
                target_id = int(input("\nEnter task ID to remove: "))
                confirm = input(f"Are you sure you want to delete task {target_id}? (y/n): ").strip().lower()

                if confirm == "y":
                    manager.RemoveTask(target_id)
                    print(f"SUCCESS: Task {target_id} has been removed.")
                else:
                    print("Deletion cancelled.")

        elif choice == '5':
            print("\n--- Filter by Priority ---")
            for idx, p in enumerate(priorities):
                print(f"{idx + 1}. Show only {p}")
            print(f"{len(priorities) + 1}. Back to all tasks")
            
            p_choice = input(f"Select (1-{len(priorities) + 1}): ")
            
            try:
                p_idx = int(p_choice) - 1
                if 0 <= p_idx < len(priorities):
                    selected_priority = priorities[p_idx]
                    filtered = FilterByPriority(manager.get_tasks(), selected_priority) #
                    print(f"\n--- Results for {selected_priority} ---")
                    display_tasks(filtered, empty_message="No tasks with this priority")
                else:
                    display_tasks(manager.get_tasks())
            except ValueError:
                print("Invalid input. Showing all tasks.")
                display_tasks(manager.get_tasks())

        elif choice == '6':
            current_filtered_list = manager.get_tasks()

            print("\nStep 1: Filter by completion status")
            print("1. Completed only")
            print("2. In-progress only")
            print("3. Skip (Show both)")
            comp_choice = input("Select (1/2/3): ").strip()

            if comp_choice == "1":
                current_filtered_list = FilterByCompletion(current_filtered_list, True)
            elif comp_choice == "2":
                current_filtered_list = FilterByCompletion(current_filtered_list, False)

            print("\nStep 2: Filter by priority")
            for idx, priority in enumerate(priorities):
                print(f"{idx + 1}. {priority}")
            print(f"{len(priorities) + 1}. Skip (Show all priorities)")

            p_choice = input(f"Select (1-{len(priorities) + 1}): ").strip()
            applied_priority_filter = False

            try:
                p_idx = int(p_choice) - 1
                if 0 <= p_idx < len(priorities):
                    selected_priority = priorities[p_idx]
                    current_filtered_list = FilterByPriority(current_filtered_list, selected_priority)
                    applied_priority_filter = True
            except ValueError:
                pass

            print("\n--- Filtered Results ---")
            msg = "No tasks with this priority" if applied_priority_filter else "No tasks found"
            display_tasks(current_filtered_list, empty_message=msg)

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()