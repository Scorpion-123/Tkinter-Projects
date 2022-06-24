from tkinter import *

root = Tk()
root.geometry("300x150")

New_Label = Label(root, text="New Window", pady=10, padx=10)
New_Label.grid(row=0, column=0)

def new_window():
    # The toplevel function helps to create a new window.
    new = Toplevel()
    new.title("I am a new Window")
    new_label = Label(new, text="I am a new window label", pady=10, padx=10)
    new_label.pack()

# Whenever the button is clicked the new window pops up because whenever the button is clicked the new window 
# creating function is executed.
New_Button = Button(root, text="Get New Window", pady=10, padx=10, command=new_window)
New_Button.grid(row=0, column=1)


root.mainloop()
