import ssl
from email.message import EmailMessage

import smtplib
import random

email_sender = 'passlock33@gmail.com'
email_password = 'zjol wlas lfzg meii'
email_receiver = 'barryjallen475@gmail.com'


#defining the subject and the body of the mail
subject = "New mail"
body = "this is crazy"+ " " +str(random.randint(1000,10000))

#Instantiating EmailMessage Library by creating an object called em
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


#to add security we import ssl for keeping an internet connection secure
#when sending important data
context = ssl.create_default_context()
#defining the email server, port and context
def verification():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

