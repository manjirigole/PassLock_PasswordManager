from CTkMessagebox import CTkMessagebox
import customtkinter
from customtkinter import CTkLabel

passp = customtkinter.CTk()
passp.geometry("700x500")
passp.resizable(False,False)
header_socials = customtkinter
#header_socials.place(x=250,y=70)

tabview = customtkinter.CTkTabview(passp)
tabview.place(x=215,y=100)

tabview.add("Save your Passwords")  # add tab at the end
tabview.set("Save your Passwords")  # set currently visible tab
l1 = customtkinter.CTkLabel(text="Enter Password",
                            font=("Helvetica",18,"bold"),
                            master=tabview.tab("Save your Passwords"))
l1.place(x=75,y=20)

e1 = customtkinter.CTkEntry(width=200,
                            font=("Helvetica",18,"bold"),
                            master = tabview.tab("Save your Passwords"))
e1.place(x=40,y=60)
def get_value():
    s1 = CTkMessagebox(title="Password Saved",
                  message=("Password has been saved successfully!"),master=tabview.tab("Save your Passwords"))

b1 = customtkinter.CTkButton(text="Save",
                             font=("Helvetica",15,"bold"),
                             master=tabview.tab("Save your Passwords"),
                             command=get_value)
b1.place(x=70,y=120)

def p_get():
    s1 = CTkMessagebox(title="Show Password",
                  message=("Password is ",str(e1.get())) ,master=tabview.tab("Save your Passwords"))

b2 = customtkinter.CTkButton(text="Show Password",
                             font=("Helvetica",15,"bold"),
                             master=tabview.tab("Save your Passwords"),
                             command=p_get)
b2.place(x=70,y=170)
passp.mainloop()