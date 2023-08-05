from tkinter import *
import customtkinter
import loginconnection

masterkey = customtkinter.CTk()
masterkey.geometry("700x500")
masterkey.configure(bg="#e1e7fd")
masterkey.resizable(False, False)
def nextpage():
    masterkey.destroy()
    import categories

#def userDetails():
    #print("values ", "", "--")


#userName = "aa"
#passVal = "bb"

firstname = customtkinter.CTkLabel(text="Enter your Username",
              font=("Helvetica",18,"bold"),master=masterkey)
firstname.place(x=250,y=100)
firstname_entry = customtkinter.CTkEntry(font=("Helvetica",16,"bold"),width=150,master=masterkey)
firstname_entry.place(x=267,y=150)

mkey = customtkinter.CTkLabel(text="Enter your Master Key",
              font=("Helvetica",18,"bold"),master=masterkey)
mkey.place(x=250,y=200)
mkey_entry = customtkinter.CTkEntry(font=("Helvetica",16,"bold"),width=150,master=masterkey)
mkey_entry.place(x=267,y=250)




#a,b = loginpage.ldetails()

mpin_button = customtkinter.CTkButton(text="Set Pin",
                     font=("Helvetica", 16, "bold"),
                     master=masterkey,
                     width=150,
                     command=lambda: [loginconnection.dbconn(firstname_entry.get(),mkey_entry.get()), nextpage()]

                     )
mpin_button.place(x=267,y=350)
masterkey.mainloop()
