from tkinter import *
from tkinter import messagebox

import radio as radio
import customtkinter

import databaseconnection
import demo_email
import pymysql

from CTkMessagebox import CTkMessagebox


def show_checkmark():
    # Show some positive message with the checkmark icon
    CTkMessagebox(message="One-Time-Password has been sent to your Mail.\n"
                          "Please go to the next page to Verify",
                  icon="check", option_1="Thanks")


def nextpage():
    import otp_page1


def selection():
    selection = radio.get()


registrationp = customtkinter.CTk()

frame2 = Frame(registrationp)
registrationp.geometry("700x600")
registrationp.configure(bg="#e1e7fd")
registrationp.resizable(False, False)

header_line2 = customtkinter.CTkLabel(text="Sign Up to PassLock",
                                      font=("Helvetica", 24, 'bold'),
                                      master=registrationp)
header_line2.place(x=240, y=45)

name = customtkinter.CTkLabel(text="Name",
                              font=("Helvetica", 16, 'bold'), master=registrationp)
name.place(x=170, y=120)
name_entry = customtkinter.CTkEntry(font=("Helvetica", 12, 'bold'), master=registrationp)
name_entry.place(x=350, y=120)

last_name = customtkinter.CTkLabel(text="Last Name",
                                   font=("Helvetica", 16, 'bold'), master=registrationp)
last_name.place(x=170, y=170)
last_name_entry = customtkinter.CTkEntry(font=("Helvetica", 12, 'bold'), master=registrationp)
last_name_entry.place(x=350, y=170)

email = customtkinter.CTkLabel(text="Email",
                               font=("Helvetica", 16, 'bold'), master=registrationp)
email.place(x=170, y=220)
email_entry = customtkinter.CTkEntry(font=("Helvetica", 12, 'bold'),
                                     width=300,
                                     master=registrationp)
email_entry.place(x=350, y=220)

password2 = customtkinter.CTkLabel(text="Password",
                                   font=("Helvetica", 16, 'bold'), master=registrationp)
password2.place(x=170, y=270)
password2_entry = customtkinter.CTkEntry(font=("Helvetica", 12, "bold"),show='*',
                                         master=registrationp)
password2_entry.place(x=350, y=270)

confirm = customtkinter.CTkLabel(text="Confirm Password",
                                 font=("Helvetica", 16, 'bold'), master=registrationp)
confirm.place(x=170, y=320)
confirm_entry = customtkinter.CTkEntry(font=("Helvetica", 12, "bold"), show='*',master=registrationp)
confirm_entry.place(x=350, y=320)

def show_password_field():
    if password2_entry.cget('show') == '*':
        password2_entry.configure(show='')
    else:
        password2_entry.configure(show='*')
    if confirm_entry.cget('show') == '*':
        confirm_entry.configure(show='')
    else:
        confirm_entry.configure(show='*')
show_password = customtkinter.CTkCheckBox(text="Show Password",
                            font=("Helvetica",12,"bold"),
                            master=registrationp,
                            command=show_password_field)
show_password.place(x=270,y=370)
radio = IntVar()
r1 = customtkinter.CTkRadioButton(
    text="Male",
    font=("Helvetica", 15, 'bold'),
    variable=radio,
    master=registrationp,
    value=1,
    command=selection)
r1.place(x=130, y=420)

r2 = customtkinter.CTkRadioButton(registrationp,
                                  text="Female",
                                  font=("Helvetica", 16, 'bold'),
                                  variable=radio,
                                  value=2,
                                  command=selection)
r2.place(x=270, y=420)

r3 = customtkinter.CTkRadioButton(registrationp,
                                  text="Other",
                                  font=("Helvetica", 16, 'bold'),
                                  variable=radio,
                                  value=3,
                                  command=selection)
r3.place(x=430, y=420)

register = customtkinter.CTkButton(text="Register",
                                   font=("Helvetica", 18, "bold"),
                                   width=150,
                                   master=registrationp,
                                   command=show_checkmark
                                   )
register.place(x=160, y=500)

next = customtkinter.CTkButton(text="Next Page",
                               width=150,
                               command=lambda: [databaseconnection.dbconn(name_entry.get(), last_name_entry.get(), password2_entry.get(),confirm_entry.get()),demo_email.verification(), nextpage()],
                               font=("Helvetica", 18, "bold"),
                               master=registrationp)
next.place(x=380, y=500)

frame2.pack()


# db = pymysql.connect(host='localhost', user='root', password='Shsss@234', database='reg_form')
# cur = db.cursor()
# try:
#     query = 'create database reg_form'
#     cur.execute(query)
#     query = 'use reg_form'
#     cur.execute(query)
#     query = 'create table users(id int not null auto_increment, firstname varchar(40),' \
#             'lastname varchar(40), password varchar(60), cpass varchar(60),primary key(id))'
#     cur.execute(query)
# except:
#     cur.execute('use reg_form')
#     query = 'insert into users(firstname, lastname, password, cpass) values(%s,%s,%s,%s)'
#     print("name--", name_entry.get()," --lastname--", last_name_entry.get(),"--password--",password2_entry.get())
#     cur.execute(query, (name_entry.get(), last_name_entry.get(), password2_entry.get(), confirm_entry.get()))
#     db.commit()
#     db.close()
#     messagebox.showinfo('success', 'successful connection')

registrationp.mainloop()
