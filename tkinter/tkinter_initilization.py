from tkinter import *

root = Tk()
# Initilizing the tkinter window.
# root.title("New Game")

# label1 = Label(root, text="Hello World !!")
# # This is used to pack the elements inide the tkinter window.
# # label1.pack()
# # This is used to pack the elements inside the tkinter window as per the co-ordinates mentioned in the row
# # and the coloumn section.
# # REMEMBER : The row and coloumn positions are relative in the window dimentions.
# # REMEMBER : If you use the grid function once than u have to use the gris function for adjusting all the dimentions 
# # and co-ordinater.

# # label1.grid(row=0,column=1)

# # Creting a button widget.
# def new():
# 	# The get method is used to get the text that is present inside the input field.
# 	s = entry1.get()
# 	l = Label(root, text=s)
# 	l.grid(row=0, column=2)

# button1 = Button(root, text="Click me !!", padx=10, pady=11, command=new)
# # "padx" and "pady" are the padding options for the button.
# # The command function decides what function to do when the button is clicked . It takes in the function name that is 
# # to be runned when the button is clicked.
# button1.grid(row=0, column=1, padx=12)

# # Creating an input field.
# entry1 = Entry(root)
# entry1.grid(row=0, column=0)
# # The insert method is used for inserting the desired text in the index position as mentioned.
# entry1.insert(0, "hello there")
# # This is used for deleting the text that is present inside the text box.
# entry1.delete(0,END)



entry = Entry(root)


def click(parameter):
	entry.insert(END, str(parameter))


# For passing a definite parameter to the fnction of the button use the lambda method.
# The lambda function is used when we try to pass any parameter to the function.
button2 = Button(root, text="button2", command=lambda:click(2))
button3 = Button(root, text="button3", command=lambda:click(3))
entry.pack()
button2.pack()
button3.pack()







root.mainloop()
