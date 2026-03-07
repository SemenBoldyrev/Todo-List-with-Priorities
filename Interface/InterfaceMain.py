##
savet = []
save = [{
    'id': 1,
    'description': 'Complete project proposal',
    'priority': 'High',
    'completed': False
},
{
    'id': 2,
    'description': 'Complete project report',
    'priority': 'Medium',
    'completed': True
}]
##
commonSeparation = "="*20
minorSeparation = "-"*20

def PrintHeader(head: str):
    print(commonSeparation)
    print(head)
    print(commonSeparation)

def PrintCommonSeparation():
    print(commonSeparation)

def PrintMinorSeparation():
    print(minorSeparation)

def PrintGoodbye():
    PrintCommonSeparation()
    PrintHeader("Goodbye!")
    PrintCommonSeparation()

def DisplayAllTasks(list: list):
    if type(list) != list or len(list) == 0:
        print("No tasks yet")
        return
    for task in save:
        print(GetTaskStrAlt(task))
        if task != save[-1]:
            PrintMinorSeparation()

def GetTaskStr(task: dict) -> str:
    return f"{task['id']} - {task['description']} (Priority: {task['priority']}) - {'Done' if task['completed'] else 'In progress'}"

def GetTaskStrAlt(task: dict) -> str:
    return f"{task['id']}: \nDescription: {task['description']} \nPriority: {task['priority']} \nStatus: {'Done' if task['completed'] else 'In progress'}"

def ShowAllTasksBeauty(list: list):
    PrintHeader("Todo List")
    DisplayAllTasks(list)
    PrintCommonSeparation()

def ShowChoice(list: list) -> int:
    if type(list) != list or len(list) == 0:
        return -1
    while True:
        n=1
        for choice in list:
            print(f"{n}. {choice}")
            n += 1
        inputChoice = input("Enter the number of your choice: ")
        try:
            inputChoice = int(inputChoice)
            if 1 <= inputChoice < len(list)+1:
                return inputChoice-1
            else:
                print("Invalid choice. Please enter a number of selected action (1 -", len(list), ")")
        except ValueError:
            print("Invalid input. Please enter a number.")
        PrintCommonSeparation()

ShowAllTasksBeauty(save)
print(ShowChoice(["desc", "add", "edit", "delete", "exit"]))