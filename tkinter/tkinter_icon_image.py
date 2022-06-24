from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Ankit dey's creation !!")

# Helps to change the icon of the tkinter window.
# root.iconbitmap("path")


# The button created for quiting the programme, and the command will be "root.quit()" as it executes the tkinter window.
button1 = Button(root, text="Exit Programe", command=root.quit)
button1.grid(row=1, column=0)


# Importing images in tkinter window.
# Provide the path of the desired image that is to be entered and the pillow module will set the image in the tkinter 
# window.
image_obj = ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\Downloads\\japanese-dragon.png"))
label1 = Label(image=image_obj)
label1.grid(row=0, column=0)








root.mainloop()
