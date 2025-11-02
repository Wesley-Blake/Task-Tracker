#import toDoList
from toDoList import ToDoListCLI

task = ToDoListCLI()
loop = True

while(loop):
    task.listTasks()
    command = input("""
    What would you like to do?
    add [a],
    remove [r],
    list [l]
    """)
    match command:
        case "a":
            temp = input("Task: ")
            if len(temp) > 0: task.add(temp)
        case "r":
            temp = input("Task: ")
            if len(temp) > 0: task.remove(temp)
        case _:
            temp = input("Do you want to continue? [Y/n]")
            if temp.lower() == "y":
                continue
            else:
                loop = False