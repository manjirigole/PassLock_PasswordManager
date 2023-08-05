from tkinter import *
import tkinter.messagebox
import customtkinter
from CTkMessagebox import CTkMessagebox
ecom= customtkinter.CTk()
ecom.geometry("700x500")
ecom.resizable(False,False)

header2 = customtkinter.CTkLabel(text='My Passwords',
                font=('Helvetica', 20, 'bold'),
                master=ecom
                )
header2.place(x=310,y=70)
def amazon():
    CTkMessagebox(title="Amazon",
                  message="Amazon\nPassword: 123456")
amazon = customtkinter.CTkButton(ecom,
                        text="Amazon",
                        command=amazon,
                        )
amazon.place(x=190,y=150)

def nykaa():
    CTkMessagebox(title="Nykaa",
                  message="Nykaa\nPassword: 123456")
nykaa = customtkinter.CTkButton(ecom,
                        text="Nykaa",
                        command=nykaa,
                        )
nykaa.place(x=190,y=200)
def ajio():
    CTkMessagebox(title="Ajio",
                  message="Ajio\nPassword: 123456")
ajio = customtkinter.CTkButton(ecom,
                        text="Ajio",
                        command=ajio,
                        )
ajio.place(x=190,y=250)

def myntra():
    CTkMessagebox(title="Myntra",
                  message="Myntra\nPassword: 123456")
myntra = customtkinter.CTkButton(ecom,
                        text="Myntra",
                        command=myntra,
                        )
myntra.place(x=400,y=150)

def flipkart():
    CTkMessagebox(title="Flipkart",
                  message="Flipkart\nPassword: 123456")
flipkart = customtkinter.CTkButton(ecom,
                        text="Flipkart",
                        command=flipkart,
                        )
flipkart.place(x=400,y=200)

def ebay():
    CTkMessagebox(title="Ebay",
                  message="Ebay\nPassword: 123456")
ebay = customtkinter.CTkButton(ecom,
                        text="Ebay",
                        command=ebay,
                        )
ebay.place(x=400,y=250)
def prev_cat():
    import categories
    ecom.destroy()

nextButton = customtkinter.CTkButton(text="Go Back",
                                     font=('Helvetica', 16, 'bold'),
                                     master=ecom,
                                     width=150,
                                     height=30,
                                     command=prev_cat)
nextButton.place(x=50,y=450)
ecom.mainloop()