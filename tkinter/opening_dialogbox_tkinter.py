from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()

def open_dialog():
    # This askopenfilename fucntion open's the dialog box and it takes several arguments like the initial file path to open the title of the dialog box and the different filetype selection options.
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\ankit\\Desktop\\new", title="File Open", filetypes=(("png files", "*.png"), ("all files", "*.*"), ("python files", "*.py"), ("html files", "*.svg")))
    # The filename variable contains the path of the selected file that u will choose to open.
    
    new_image = ImageTk.PhotoImage(Image.open(filename))
    Image_label = Label(root, image=new_image)
    Image_label.image=new_image
    Image_label.pack()


open_dialog_button = Button(root, text="Open Dialog", command=open_dialog, padx=10, pady=10)
open_dialog_button.pack()





root.mainloop()
