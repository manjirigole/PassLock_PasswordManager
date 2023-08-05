from CTkMessagebox import CTkMessagebox
import customtkinter
from customtkinter import CTkLabel

socials = customtkinter.CTk()
socials.geometry("700x500")
socials.resizable(False,False)
header_socials = customtkinter.CTkLabel(text="Socials",
                                        font=("Helvetica",24,"bold"),
                                        master=socials)
header_socials.place(x=305,y=70)

def insta():
    socials.destroy()
    import passpage
instagram = customtkinter.CTkButton(socials,
                        text="Instagram",
                        font=('Helvetica', 16),
                        command=insta,
                        )
instagram.place(x=150,y=150)

def pin():
    socials.destroy()
    import passpage
pinterest = customtkinter.CTkButton(socials,
                        text="Pinterest",
                        font=('Helvetica', 16),
                        command=pin,
                        )
pinterest.place(x=150,y=250)
def face():
    socials.destroy()
    import passpage
facebook = customtkinter.CTkButton(socials,
                        text="Facebook",
                        font=('Helvetica', 16),
                        command=face,
                        )
facebook.place(x=150,y=350)

def twitter():
    socials.destroy()
    import passpage
twitter = customtkinter.CTkButton(socials,
                        text="Twitter",
                        font=('Helvetica', 16),
                        command=twitter,
                        )
twitter.place(x=400,y=150)

def you():
    socials.destroy()
    import passpage
youtube = customtkinter.CTkButton(socials,
                        text="Youtube",
                        font=('Helvetica', 16),
                        command=you,
                        )
youtube.place(x=400,y=250)

def red():
    socials.destroy()
    import passpage
Reddit = customtkinter.CTkButton(socials,
                        text="Reddit",
                        font=('Helvetica', 16),
                        command=red,
                        )
Reddit.place(x=400,y=350)

def prev_cat():
    import categories
    socials.destroy()

nextButton = customtkinter.CTkButton(text="Go Back",
                                     font=('Helvetica', 16, 'bold'),
                                     master=socials,
                                     width=150,
                                     height=30,
                                     command=prev_cat)
nextButton.place(x=50,y=25)


socials.mainloop()