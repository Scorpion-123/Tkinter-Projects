from tkinter import *

root = Tk()

# The dropdown use a variable which stores the value of the selected dropdown.
var = StringVar()
var_list = ["Mon", "Tues", "Wed"]
# The OptionMenu function takes the master window name and takes the variable name and the options of the dropdown.                                                           
# There are two methods of using the options in the OptionMenu function.
# c = OptionMenu(root, var, *var_list)
c = OptionMenu(root, var, "Mon", "Tues", "Wed")
c.pack()

def get_result():
    new_label = Label(root, text=var.get())
    new_label.pack()

btn = Button(root, text="Get Result", command=get_result)
btn.pack()

root.mainloop()
