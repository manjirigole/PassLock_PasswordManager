import random
import customtkinter
from tkinter import *
import demo_email
from CTkMessagebox import CTkMessagebox

otp_page1 = customtkinter.CTk()
otp_page1.geometry("700x500")
otp_header = customtkinter.CTkLabel(text="Verify your PassLock Account",
                   font=("Helvetica", 24, "bold"),
                   master=otp_page1
                   )
otp_header.place(x=180,y=100)
otp_body = customtkinter.CTkLabel(text="Enter the OTP sent to your registered mail",
                   font=("Helvetica", 18, "bold"),
                   master=otp_page1
                   )
otp_body.place(x=180,y=185)
otp_entry = customtkinter.CTkEntry(font=("Helvetica",12,"bold"),master=otp_page1,
                                   width=150)
otp_entry.place(x=270,y=230)

def checkmark():
    show_check = CTkMessagebox(message="Your account has been verified successfully!",
                               icon="check",option_1="Thanks",
                               master=otp_page1,
                               )
otp_button = customtkinter.CTkButton(text="Verify Account",
                      font=("Helvetica",18,"bold"),
                      width=200,
                      master=otp_page1,
                      command=checkmark
                     )
otp_button.place(x=248,y=350)


def next_page():
    import masterkeypage
    otp_page1.destroy()
next = customtkinter.CTkButton(text="Next Page",
                               font=("Helvetica",18,"bold"),
                               master=otp_page1,
                               width=150,
                               command=next_page)
next.place(x=270,y=400)


otp_page1.mainloop()