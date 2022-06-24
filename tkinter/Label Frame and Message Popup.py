from tkinter import *
from tkinter import messagebox

root = Tk()
# Creating a Label Frame object and packing it inside the root window.
label = LabelFrame(root, text="This is a label", padx=10, pady=20)
label.pack(anchor=S)

# Showing a popup when the button inside the popup is clicked.
# There are many kinds of buttons like : showerror, showwarning, showinfo, askquestion, askokcancel, askretrycancel,
# askyesno, askyesnocancel.
def popup():
    messagebox.showerror(title="This is an Info", message="How are you")
    messagebox.askretrycancel(title="Retry/Ask/Cancel", message="What are u doing")

# Packing a button inside the Label Frame object.
b = Button(label, text="click me", command=popup)
b.pack()



root.mainloop()
