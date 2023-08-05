from tkinter import *
import radio as radio
import customtkinter
getstarted = customtkinter.CTk()
getstarted.geometry("700x500")
getstarted.configure(bg="#e1e7fd")
getstarted.resizable(False,False)
def nextpage():
    getstarted.destroy()
    import registrationpage
def nextpage_login():
    getstarted.destroy()
    import loginpage
def prevpage():
    getstarted.destroy()
    import masterkeypage
def prevpage_login():
    getstarted.destroy()
    import masterkeypage


lineA = customtkinter.CTkLabel(text="Safe Place\n"
              "for all your\n"
              "passwords",
              font=("Helvetica",35,"bold"),
              master=getstarted)
lineA.place(x=270, y=160)

b1 = customtkinter.CTkButton(text="Register",
            font=("Helvetica", 16, "bold"),
            width=120,
            master=getstarted,
            corner_radius=8,
            command=nextpage
            )
b1.place(x=200,y=350)

b2 = customtkinter.CTkButton(text="Login",
            font=("Helvetica", 16, "bold"),
            width=120,
            master=getstarted,
            corner_radius=8,
            command=nextpage_login
            )
b2.place(x=400,y=350)
getstarted.mainloop()