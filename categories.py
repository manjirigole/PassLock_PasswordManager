from tkinter import *
import customtkinter
category = customtkinter.CTk()
category.geometry("700x500")
category.configure(bg="#e1e7fd")
category.resizable(False, False)
def socials():
    category.destroy()
    import socials
def ecommerce():
    category.destroy()
    import ecommerce
def banking():
    category.destroy()
    import banking


header = customtkinter.CTkLabel(text='Password Vault',
               font=('Helvetica',24,'bold'),
               master=category
               )
header.place(x=270,y=50)
###socials, ecoomerce, banking, gmails, drive
socials =  customtkinter.CTkButton(text='Socials',
                  font=('Helvetica',16,'bold'),
                  width=150,
                  height = 30,
                  command=socials,
                  master=category,
                  )
socials.place(x=150,y=150)
ecommerce = customtkinter.CTkButton(text='E-Commerce',
                  font=('Helvetica',16,'bold'),
                  width=150,
                  height = 30,
                  master=category,
                   command=ecommerce
                   )
ecommerce.place(x=150,y=250)

banking = customtkinter.CTkButton(text='Banking',
                  font=('Helvetica',16,'bold'),
                  master=category,
                  width=150,
                  height = 30,
                 command=banking
                 )
banking.place(x=150,y=350)

gmail = customtkinter.CTkButton(text='Gmail',
                  font=('Helvetica',16,'bold'),
                  master=category,
                  width=150,
                  height = 30,
               #command=nextpage
               )
gmail.place(x=400,y=150)

address = customtkinter.CTkButton(text='Addresses',
                  font=('Helvetica',16,'bold'),
                  master=category,
                  width=150,
                  height = 30,
               #command=nextpage
                 )
address.place(x=400,y=250)

wifi = customtkinter.CTkButton(text='WiFi Passwords',
                  font=('Helvetica',16,'bold'),
                  master=category,
                  width=150,
                  height = 30,
              # command=nextpage
              )
wifi.place(x=400,y=350)


category.mainloop()
