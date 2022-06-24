from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import tkinter
import sqlite3


def main_window():
    global root_window
    
    root_window = Tk()
    root_window.geometry('500x520')
    root_window.title('International Bank')
    root_window.configure(bg='#3CAEA3')

    bank_label = Label(root_window, text='International Bank',
                       fg='yellow', bg='black', font=('Times',20), padx=5)
    bank_label.pack()

    # This is the Bnak Image section.
    image_frame = Frame(root_window, width=100, height=100)
    image_frame.pack()
    
    bank_image = ImageTk.PhotoImage(Image.open('Bank.jpg'))

    label = Label(image_frame, image=bank_image)
    label.pack()

    # The Buttons section.
    create_account_button = Button(root_window, text='Create A New Account',
                                   padx=7, fg='#070bf2', bg='#27f207', command=create_account_entries)
    create_account_button.place(y=470, x=100)

    login_button = Button(root_window, text='Login To Existing Account',
                          padx=7, fg='yellow', bg='red', command=Login)
    login_button.place(y=470, x=250)

    
    root_window.mainloop()


def create_account_entries():
    # Here we are globalising the keywords so that
    # we can get access to the entry fields in any other function.
    global user_name_entry, account_balance_entry, address_entry, phone_number_entry
    global secret_question_entry, secret_question_combobox, email_entry


    # The Available Security questions.
    secret_questions = ['Whats Your Favourite Color ?',
                        'Whats Your Favourite Food ?',
                        'Whats Your Favourite Place ?',
                        'Whats Your Favourite Season ?',
                        'Whats Your Favourite Weather ?',
                        'Whats Your Favourite Day ?']
       
    login_window = Toplevel(root_window)
    login_window.title('Create Account')
    login_window.geometry('410x310')

    header = Label(login_window, text='Create A New Account',
                   fg='yellow', bg='black', font=('Times',20), padx=5)
    header.pack()

    user_name = Label(login_window, text='User Name :',
                      font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    user_name.place(y=50, x=20)
    user_name_entry = Entry(login_window, width=30)
    user_name_entry.place(y=50, x=150)

    account_balance = Label(login_window, text='Initial Account Balance :',
                            font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    account_balance.place(y=80, x=20)
    account_balance_entry = Entry(login_window, width=30)
    account_balance_entry.place(y=80, x=200)
    
    address = Label(login_window, text='Address :',
                    font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    address.place(y=110, x=20)
    address_entry = Entry(login_window, width=30)
    address_entry.place(y=110, x=150)

    phone_number = Label(login_window, text='Phone Number :',
                         font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    phone_number.place(y=140, x=20)
    phone_number_entry = Entry(login_window, width=30)
    phone_number_entry.place(y=140, x=150)

    email = Label(login_window, text='Email Id :',
                  font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    email.place(y=170, x=20)
    email_entry = Entry(login_window, width=30)
    email_entry.place(y=170, x=150)

    secret_question_combobox = ttk.Combobox(login_window, values = secret_questions, width=30)
    secret_question_combobox.set('Select Your Secret Question !!')
    secret_question_combobox.place(y=200, x=20)

    secret_question_answer = Label(login_window, text='Secret Question Answer : ',
                         font=('Arial', 12), bg='#f51505', fg='yellow', padx=5)
    secret_question_answer.place(y=230, x=20)
    secret_question_entry = Entry(login_window, width=30)
    secret_question_entry.place(y=230, x=220)

    create_account_button = Button(login_window, text='Create Account',
                                   bg='#27f207', fg='#070bf2', padx=7, command=create_account)
    create_account_button.place(y=270, x=145)
    

def create_account():
    user_name = user_name_entry.get()
    account_bal_initial = account_balance_entry.get()
    address = address_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    secret_question = secret_question_combobox.get()
    secret_question_answer = secret_question_entry.get()

    if user_name == '' or account_bal_initial == '' or address == '' or phone_number == '' or email == '' or secret_question_answer == '' or secret_question == 'Select Your Secret Question !!':
        messagebox.showwarning(title='Warning..', message='Please Enter all the fields carefully !!')
    else:
    #   messagebox.askokcancel(title='Login Successfull', message='The fields have been successfully inserted.')
        messagebox.askyesno(title='Warning..', message="Remember The Data Entered During Sign Up can't be modified so please check the data carefully before procedding. Do you want to proceed ??")
        
        
        
def Login():
    pass
    
    
main_window()
