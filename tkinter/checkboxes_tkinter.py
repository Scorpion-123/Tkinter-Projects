from tkinter import *

root = Tk()

# The checkbox use a variable which stores the value of the checkbox.
var = IntVar()

# The Checkbutton uses a variable used for storeing the selected value in the checkbox.
c = Checkbutton(root, text="Check Me", variable=var)
c.pack()

def check_details():
    # We can get the var selection using the .get() method.
    new = Label(root, text=var.get())
    new.pack()

btn = Button(root, text="Checkbox details", command=check_details)
btn.pack()

root.mainloop()