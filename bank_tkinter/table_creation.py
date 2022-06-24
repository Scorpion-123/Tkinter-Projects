import sqlite3

database_instance = sqlite3.connect('bank_database.db')
y_cursor = database_instance.cursor()

y_cursor.execute('''Create table bank_user
                    (user_name varchar(30) unique not null,
                     bank_account_number int(14) primary key,
                     account_balance varchar(20) not null,
                     address varchar(100) not null,
                     security_question varchar(50) not null,
                     security_answer varchar(40) not null,
                     phone_number int(10) not null,
                     email varchar(30) not null) ''')

database_instance.commit()

