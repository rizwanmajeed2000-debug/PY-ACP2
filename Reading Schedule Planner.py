
from tkinter import *

def open_planner():
    window = Toplevel(root)
    window.title("Reading Schedule Planner")
    window.geometry("300x250")

    Label(window, text="Total pages in book:").grid(row=0, column=0, padx=5, pady=5)
    total_entry = Entry(window)
    total_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(window, text="Pages per day:").grid(row=1, column=0, padx=5, pady=5)
    daily_entry = Entry(window)
    daily_entry.grid(row=1, column=1, padx=5, pady=5)

    def calculate():
        try:
            total = int(total_entry.get())
            daily = int(daily_entry.get())

            if total <= 0 or daily <= 0:
                result.config(text="Enter positive numbers!")
                return

            days = total // daily
            remaining = total % daily

            result.config(
                text="Complete days: " + str(days) +
                "\nRemaining pages: " + str(remaining)
            )

        except ValueError:
            result.config(text="Please enter valid numbers!")

    Button(window, text="Calculate", command=calculate).grid(
        row=2, column=0, columnspan=2, pady=10
    )

    result = Label(window, text="")
    result.grid(row=3, column=0, columnspan=2, pady=5)


root = Tk()
root.title("Reading Schedule Planner")
root.geometry("300x150")

Label(root, text="Welcome to the Reading Planner!").grid(
    row=0, column=0, padx=20, pady=15
)

Button(root, text="Open Planner", command=open_planner).grid(
    row=1, column=0, pady=10
)

root.mainloop()
