from tkinter import *

root = Tk()

# NOTE: The value of the slider can be accessed using the .get() method.

# Initially the slider is oriented vertically.
vertical = Scale(root, from_=0, to=200)
vertical.pack()

def value_get():
    new = Label(root, text=vertical.get())
    new.pack()
    
# We can change the orientation of the silder and can make it HORIZONTAL.
horizintal = Scale(root, from_=10, to=200, orient=HORIZONTAL)
horizintal.pack()

new_button = Button(root, text="Button Value", command=value_get)
new_button.pack()
root.mainloop()

