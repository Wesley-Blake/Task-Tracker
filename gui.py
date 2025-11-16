from toDoList import ToDoList
from tkinter import *
import tkinter as tk
from tkinter import ttk

def printing(event):
    #print("Test:", test.get())
    if tasks.add(container.get()):
        container.set("")
        listboxtest.insert(END, tasks.list_of_tasks[-1])
    else:
        container.set("")


tasks = ToDoList()

root = tk.Tk()
root.geometry("400x400")
fontsize = ("Arial", 20)
root.title("To Do List")

listboxtest = Listbox(font=fontsize)
listboxtest.pack()


test = tk.Entry(font=fontsize)
test.pack()
container = tk.StringVar()
container.set("Test entry")
test["textvariable"] = container
test.bind('<Key-Return>', printing)


#message = tk.Label(root, text = "To Do List")
#message.pack()

root.mainloop()