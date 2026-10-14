
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Routine Checker")
root.geometry("300x300")

def check():
    if task.get() == "":
        messagebox.showwarning("Warning", "Enter a task!")
    else:
        result.config(text="Task: " + task.get())

def next_task():
    result.config(text="Next task: Revision")

def typing(event):
    result.config(text="Last character: " + task.get()[-1])

def click(event):
    result.config(text="You clicked!")

Label(root, text="After-School Routine").pack()

task = Entry(root)
task.pack()

task.bind("<KeyRelease>", typing)

Button(root, text="Check Task", command=check).pack()
Button(root, text="Next Task", command=next_task).pack()

area = Label(root, text="Click Here", bg="lightblue")
area.pack(pady=10)
area.bind("<Button-1>", click)

result = Label(root, text="")
result.pack()

root.mainloop()
