##################################################
#
# Simple to list with gui
#
##################################################

class ToDoListCLI:
    def __init__(self):
        # list to hold tasks
        self.__list_of_tasks = []
    # List tasks
    def listTasks(self):
        for item in self.__list_of_tasks:
            print(item)
    # Add task
    def add(self, item: str):
        self.__list_of_tasks.append(item)
    # Delete task
    def remove(self, item: str):
        try:
            self.__list_of_tasks.remove(item)
        except:
            print(f"Item: {item}, not in tasks.")



if __name__ == "__main__":
    test = ["trash", "Luandry", "dishes"]

    try:
        myTest = ToDoListCLI()
    except:
        print("Failed to instantiate ToDoListCLI.")

    try:
        for item in test:
            myTest.add(item)
    except:
        print("Failed to add items from test list to tasks.")
    
    myTest.remove("trash")
    myTest.tasks()