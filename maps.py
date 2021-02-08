import smtplib
from email.message import EmailMessage
import imghdr
import os

email_adress =  "eswar.bbid@gmail.com"
password =  "eswar@1234"
msg = EmailMessage()
msg['Subject'] = 'MAPS'
msg['From'] = email_adress   
msg['To'] = email_adress   #it can be list for multiple contacts
msg.set_content('FIND MAP RECRUIT')
html_m = open("prac.html").read()
print(html_m)
msg.add_alternative(html_m,subtype ='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_adress,password)
    smtp.send_message(msg)

