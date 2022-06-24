from tkinter import *

root = Tk()
root.title("Simple Calculator...")

entry1 = Entry(root, width=30)
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Code Logic : Whenever the function buttons are pressed then the functions specific to that button is activated and 
#              the function has a global variable named calculation which decides what operation to perform when the
#              equal button is pressed .It assigns a global variable that decides what to do accordingly.

#              The main function is in the equal button where the calculations are performed as per the buttons clicked
#              by the user.            



def click(parameter):
    entry1.insert(END, parameter)


def add():
    global s
    global calculation
    calculation = "add"
    s = float(entry1.get())
    entry1.delete(0, END)


def equals():
    m = entry1.get()
    entry1.delete(0, END)
    if m == "":
        entry1.insert(0, "Enter valid number and Functions !!")
    if calculation == "add":
        entry1.insert(0, float(m)+s)
    elif calculation == "subs":
        entry1.insert(0,first_element-float(m))
    elif calculation == 'mul':
        entry1.insert(0,a*float(m))
    elif calculation == "div":
        if m == 0:
            entry1.insert(0,"Can't divide by Zero !!")
        else:
            entry1.insert(0,str(round(w/float(m),5)))
    


def mul():
    global a
    global calculation
    a = float(entry1.get())
    calculation = "mul"
    entry1.delete(0,END)


def divi():
    global w
    global calculation
    calculation = "div"
    w = float(entry1.get())
    entry1.delete(0,END)


def clear():
    # Getting the length of the word.
    s = len(entry1.get())
    m = entry1.get()[0]
    if m.isalpha():
        entry1.delete(0,END)
    # Deleting the last element from the text.
    else:
        entry1.delete(s-1, s)


def allclear():
    entry1.delete(0, END)


def subs():
    global first_element
    first_element = float(entry1.get())
    global calculation
    calculation = "subs"
    entry1.delete(0,END)


def dot():
    entry1.insert(END,".")


button1 = Button(root, text="1", padx=40/3, pady=10, command=lambda: click(1))
button2 = Button(root, text="2", padx=40/3, pady=10, command=lambda: click(2))
button3 = Button(root, text="3", padx=40/3, pady=10, command=lambda: click(3))
button4 = Button(root, text="4", padx=40/3, pady=10, command=lambda: click(4))
button5 = Button(root, text="5", padx=40/3, pady=10, command=lambda: click(5))
button6 = Button(root, text="6", padx=40/3, pady=10, command=lambda: click(6))
button7 = Button(root, text="7", padx=40/3, pady=10, command=lambda: click(7))
button8 = Button(root, text="8", padx=40/3, pady=10, command=lambda: click(8))
button9 = Button(root, text="9", padx=40/3, pady=10, command=lambda: click(9))
button0 = Button(root, text="0", padx=60/3, pady=10, command=lambda: click(0))
button_ac = Button(root, text="All Clear", padx=36 /
                   3, pady=10, command=allclear)
button_equals = Button(root, text="=", padx=36/3, pady=10, command=equals)
button_add = Button(root, text="+", padx=40/3, pady=10, command=add)
button_subs = Button(root, text="-", padx=40/3, pady=10, command=subs)
button_clear = Button(root, text="Clear", padx=36/3, pady=10, command=clear)
button_mul = Button(root, text="*", padx=40/3, pady=10, command=mul)
button_div = Button(root, text="/", padx=40/3, pady=10, command=divi)
button_dot = Button(root, text=".", padx=40/3, pady=10, command=dot)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button_equals.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=4, column=2)


button0.grid(row=5, column=0)
button_subs.grid(row=5, column=2)
button_ac.grid(row=5, column=1, padx=30)

button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1, padx=20)
button_dot.grid(row=6, column=2)

root.mainloop()


