from tkinter import *
import customtkinter
bank = customtkinter.CTk()
bank.geometry("700x500")
bank.configure(bg="#e1e7fd")
bank.resizable(False,False)
header2 = customtkinter.CTkLabel(text="My Accounts",
                font=("Helvetica",24,"bold"),
                master=bank
                )
header2.place(x=290,y=100)
def bank1():
    bank.destroy()
    import BankA
def bank2():
    bank.destroy()
    import BankB

button1 = customtkinter.CTkButton(text="Account1",
            font=("Helvetica", 16, "bold"),
            master=bank,
            width=20,
            command=bank1
            )
button1.place(x=315,y=190)

button2 = customtkinter.CTkButton(text="Account2",
            font=("Helvetica", 16, "bold"),
            master=bank,
            width=20,
            command=bank2
            )
button2.place(x=315,y=250)
def prev_cat():
    import categories
    bank.destroy()

nextButton = customtkinter.CTkButton(text="Go Back",
                                     font=('Helvetica', 16, 'bold'),
                                     master=bank,
                                     width=150,
                                     height=30,
                                     command=prev_cat)
nextButton.place(x=50,y=450)
bank.mainloop()