from tkinter import *
import tkinter.messagebox
master = Tk()
master.geometry("500x500")




def opennewWindow():
    newWindow1 = Toplevel(master)
    newWindow1.geometry("400x400")
    newWindow1.title("Login/Register")

    def login():
        newWindow3 = Toplevel(newWindow1)
        newWindow3.title = "Login"
        newWindow3.geometry("500x350")

        Username2 = Label(newWindow3,
                          text="Username",
                          font=('Arial', 10, 'bold')
                          )
        Username2.place(x=100, y=100)
        Username2_Entry = Entry(newWindow3,
                                font=('Arial', 10, 'bold')
                                )
        Username2_Entry.place(x=180, y=100)

        password2 = Label(newWindow3,
                          text = "Password",
                          font = ('Arial',10, 'bold')
                          )
        password2_entry = Entry(newWindow3,
                                font = ('Arial', 10, 'bold')
                                )
        password2.place(x=100, y=150)
        password2_entry.place(x=180, y=150)

        Login2 = Button(newWindow3,
                        text="Login",
                        font=('Arial', 10, 'bold'),
                        fg="#8f65ad",
                        activeforeground="#694285",
                        activebackground="black",
                        width="15",
                        height="2",
                        command = "account"
                        )
        Login2.place(x=190,y=200)


    def registration():
        newWindow2 = Toplevel(newWindow1)
        newWindow2.geometry("700x300")
        newWindow2.title("Registration")

        def onClick():
            tkinter.messagebox.showinfo("Account", "Account created successfully")


        Name = Label(newWindow2,
                               text="Name",
                               font=('Arial',10,'bold'),
                               )
        Name.place(x=95, y=35)
        Name_Entry= Entry(newWindow2,
                                     font=('Arial',10,'bold'),
                                    )
        Name_Entry.place(x=190, y=35)

        Surname = Label(newWindow2,
                        text="Surname",
                        font=('Arial',10,'bold')
                        )
        Surname.place(x=400, y= 35)
        Surname_Entry = Entry(newWindow2,
                              font=('Arial',10,'bold')
                              )
        Surname_Entry.place(x=495, y=35)

        Email_Regis = Label(newWindow2,
                            text="Email",
                            font=('Arial',10,'bold'),
                            )
        Email_Regis.place(x=95, y=75)
        Email_Entry = Entry(newWindow2,
                            font=('Arial',10, 'bold'),
                            width="40",
                            )
        Email_Entry.place(x=190, y=75)

        password_R = Label(newWindow2,
                         text = "Password",
                         font = ('Arial', 10, 'bold'))
        password_R.place(x=95, y=115)
        password_Entry = Entry(newWindow2,
                               font=('Arial', 10, 'bold')
                               )
        password_Entry.place(x=190,y=115)
        confirm_password = Label(newWindow2,
                         text="Confirm Password",
                         font= ('Arial',10, 'bold')
                                )
        confirm_password.place(x=95,y=155)
        confirm_password_entry = Entry(newWindow2,
                                       font=('Arial',10,'bold'))
        confirm_password_entry.place(x=250,y=155)

        register2 = Button(newWindow2,
                          text = "Register",
                          font = ('Arial',10,'bold'),
                           fg = "#8f65ad",
                           activeforeground = "#694285",
                           activebackground = "black",
                           width = "15",
                           height="2",
                           command=onClick)

        register2.place(x=285, y=195)

    Login = Button(newWindow1,
                   text="Login",
                   font=('Arial', 15, 'bold'),
                   padx=10,pady=10,
                   fg="#8f65ad",
                   activeforeground="#694285",
                   activebackground="black",
                   width="15",
                   command=login)


    Register = Button(newWindow1,
                      text="Register",
                      font=('Arial', 15, 'bold'),
                      padx=10, pady=10,
                      fg="#8f65ad",
                      activeforeground="#694285",
                      activebackground="black",
                      width="15",
                      command=registration
                       )
    Register.place(x=100,y=200)
    Login.place(x=100,y=100)
label1 = Label(master,
               text="Pass",
               fg="#8f65ad",
               font=('Arial',30,'bold')
               )
label2 = Label(master,
               text="'Lock",
               fg="black",
               font=('Arial',30,'bold')
               )
getStarted = Button(master,
                    text="Get Started -->",
                    font = ('Arial',25),
                    fg = "white",
                    bg="#8f65ad",
                    activeforeground="#694285",
                    activebackground="black",
                    command = opennewWindow)

label1.place(x=150, y=100)
label2.place(x=250, y=100)
getStarted.place(x=150, y=200)




master.mainloop()