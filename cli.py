#import toDoList
import os
from platform import system
from toDoList import ToDoList

pc = system()
clear = "cls" if pc == "linux" else "clear"
task = ToDoList()
loop = True

while(loop):
    try:
        os.system(clear)
    except:
        print("Failed to clear screen, os detection error?")
        exit()
    task.listTasks()
    command = input(
"""
What would you like to do?
add [a],
remove [r],
list [l],
End [e]
"""
    )
    match command:
        case "a":
            temp = input("Task: ")
            if len(temp) > 0:
                task.add(temp)
            else:
                print(f"Failed to add task: {temp}")
        case "r":
            temp = input("Task: ")
            if len(temp) > 0: task.remove(temp)
        case "e":
            temp = input("Are you sure you want to quit? [Y/n]")
            if temp.lower() == "n":
                loop = True
            else:
                loop = False
                os.system(clear)
        case _:
            continue