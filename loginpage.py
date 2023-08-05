from tkinter import *
import customtkinter
import pymysql

def nextpage():

    a,b = ldetails()
    login_gui.destroy()
    import masterkeypage
    print(" u ", a, " p ", b)
    #masterkeypage.passVal = b
    #masterkeypage.userName = a

def prevpage():
    login_gui.destroy()
    import getstartedpage

login_gui = customtkinter.CTk()
myframe = Frame(login_gui)
login_gui.geometry("700x500")
login_gui.configure(bg="#e1e7fd")
login_gui.resizable(False,False)
#####################credentials
header_line2 = customtkinter.CTkLabel(text="Login",
                     font=("Helvetica",24,'bold'),
                     master=login_gui)
header_line2.place(x=325,y=60)

username = customtkinter.CTkLabel(text="Username",
                 font=('Helvetica',16,'bold'),
                 master=login_gui)
username.place(x=200,y=170)
username_entry = customtkinter.CTkEntry(master=login_gui,
                                        font=('Helvetica',16,'bold'),)
username_entry.place(x=350,y=170)


password = customtkinter.CTkLabel(text='Password',
                 font=('Helvetica',16,'bold'),
                master=login_gui)
password.place(x=200,y=230)
password_entry = customtkinter.CTkEntry(login_gui, font=('Helvetica',16,"bold"),
                       show='*')
password_entry.place(x=350,y=230)

def show_password_field():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
    else:
        password_entry.configure(show='*')

show_password = customtkinter.CTkCheckBox(text="Show Password",
                            font=("Helvetica",12,"bold"),
                            master=login_gui,
                            command=show_password_field)
show_password.place(x=300,y=280)

login_button = customtkinter.CTkButton(text="Login",
                      font=("Helvetica",16,"bold"),
                      width=150,
                      command=nextpage,
                      master=login_gui
                     )
login_button.place(x=270,y=370)
#uName = username_entry.get()
#pw = password_entry.get()
def ldetails():
    #print("values ", username_entry.get(), "--",password_entry.get())
    return username_entry.get(), password_entry.get()

    #return "aa","bb"


#db = pymysql.connect(host='localhost', user='root', password='Shsss@234', database='reg_form')
#cur = db.cursor()
#query = 'use reg_form'
#cur.execute(query)
#print("database connected")
#try:
 #query = 'create table login(id int not null auto_increment, username varchar(40),' \
        #'password varchar(60), mkey int, primary key(id))'
 #cur.execute(query)
#except:
    #cur.execute('use reg_form')
    #query = 'insert into login(firstname, password, mkey) values(%s,%s,%s)'
    #print("Inserting user----name--", username, " --lastname--", password, "--confirm--")
    #cur.execute(query, (username, password))
    #db.commit()
    #db.close()



#myframe.pack()
login_gui.mainloop()
##FCF5EE - cream
###6886C5