
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Letter Writing Application")
root.geometry("600x450")

def open_file():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        file = open(filename, "r")
        text_area.delete("1.0", END)
        text_area.insert("1.0", file.read())
        file.close()

def save_file():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        file = open(filename, "w")
        file.write(text_area.get("1.0", END))
        file.close()

def clear_text():
    text_area.delete("1.0", END)

# Buttons
open_button = Button(root, text="Open Letter", command=open_file)
save_button = Button(root, text="Save Letter", command=save_file)
clear_button = Button(root, text="Clear", command=clear_text)

open_button.grid(row=0, column=0, padx=5, pady=5)
save_button.grid(row=0, column=1, padx=5, pady=5)
clear_button.grid(row=0, column=2, padx=5, pady=5)

# Text area
text_area = Text(root, width=70, height=22)
text_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
