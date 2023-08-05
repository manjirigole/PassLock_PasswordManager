import customtkinter
a1 = customtkinter.CTk()
a1.geometry("700x700")
a1.configure(bg="#e1e7fd")
a1.resizable(False,False)
header3 = customtkinter.CTkLabel(text="Account Details",
                font=("Helvetica",20,"bold"),
                master=a1
                )
header3.place(x=10,y=10)
tabview = customtkinter.CTkTabview(width=500,
                                   master=a1,
                                   height=400)
tabview.place(x=100,y=50)
t1 = tabview.add("Account 1")
l1 = customtkinter.CTkLabel(text="Account Number",master=t1,
                            font=("Helvetica",17,"bold"))
l1.place(x=10,y=10)
b1 = customtkinter.CTkButton(t1)

l2 = customtkinter.CTkLabel(text="000000452278955874",master=t1,
                            font=("Helvetica",17,"bold"))
l2.place(x=250,y=10)

l3 = customtkinter.CTkLabel(text="Name",master=t1,
                            font=("Helvetica",17,"bold"))
l3.place(x=10,y=50)

l4 = customtkinter.CTkLabel(text="Bary Allen",master=t1,
                            font=("Helvetica",17,"bold"))
l4.place(x=250,y=50)

l5 = customtkinter.CTkLabel(text="Available Balance",master=t1,
                            font=("Helvetica",17,"bold"))
l5.place(x=10,y=100)

l6 = customtkinter.CTkLabel(text="Rs, 15,253",master=t1,
                            font=("Helvetica",17,"bold"))
l6.place(x=250,y=100)

l7 = customtkinter.CTkLabel(text="Uncleared Balance",master=t1,
                            font=("Helvetica",17,"bold"))
l7.place(x=10,y=150)

l8 = customtkinter.CTkLabel(text="Rs, 0.00",master=t1,
                            font=("Helvetica",17,"bold"))
l8.place(x=250,y=150)

l9 = customtkinter.CTkLabel(text="MOD Balance",master=t1,
                            font=("Helvetica",17,"bold"))
l9.place(x=10,y=200)

l10 = customtkinter.CTkLabel(text="Rs, 0.00",master=t1,
                            font=("Helvetica",17,"bold"))
l10.place(x=250,y=200)

l11 = customtkinter.CTkLabel(text="Monthly Average",master=t1,
                            font=("Helvetica",17,"bold"))
l11.place(x=10,y=250)

l12 = customtkinter.CTkLabel(text="Click for MAB",master=t1,
                            font=("Helvetica",17,"bold"))
l12.place(x=250,y=250)

l13 = customtkinter.CTkLabel(text="Currency",master=t1,
                            font=("Helvetica",17,"bold"))
l13.place(x=10,y=300)

l14 = customtkinter.CTkLabel(text="INR",master=t1,
                            font=("Helvetica",17,"bold"))
l14.place(x=250,y=300)



a1.mainloop()