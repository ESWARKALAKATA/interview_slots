'''import smtplib
from email.message import EmailMessage
import imghdr
import os


email_adress =  "eswar.bbid@gmail.com"
password =  "eswar@1234"
msg = EmailMessage()
msg['Subject'] = 'submit button task'
msg['From'] = email_adress   
msg['To'] = email_adress   #it can be list for multiple contacts
msg.set_content('this is plain text html')

msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <iframe href="https://www.google.com" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3806.1509080042115!2d78.38670781397096!3d17.452489788039575!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb9163eed6abaf%3A0xda95406d85ffcd7b!2sMapRecruit!5e0!3m2!1sen!2sin!4v1611742256005!5m2!1sen!2sin" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>

    
</body>
</html>
""",subtype ='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_adress,password)
    smtp.send_message(msg)


'''
#adding html to the email















#with smtplib.SMTP('localhost',1025) as smtp:
#python -m smtpd -n -c DebuggingServer localhost:1025

#general way
'''

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()  #identifies ourselves 
    smtp.starttls() #started encrypted connection
    smtp.login(email_adress,password)
    subject = 'test email'
    body = "do more changes in this thing you have to do it"
    #msg  = f'Subject: {subject} \n\n {body}'
    smtp.login(email_adress,password)
    smtp.sendmail(email_adress,'eswar.kalakata@gmail.com',msg)


'''
#google add attachments for to kniw the type of arguments we are passing
#adding attachments
#for tagging multiple files in perticualr directroy
'''for i in os.listdir():  
    print(i)
    with open(i,'rb') as f :
        file_data = f.read()
        file_name = f.name
        file_type =i.split(".")[1]
        print(file_type)
    msg.add_attachment(file_data, maintype = 'file',subtype = file_type,filename = file_name)

'''
#tagging single file 
'''with open('ADjB6.jpg','rb') as f :
    file_data   = f.read()
    file_name =  'docx'
    file_type  = imghdr.what(f.name)

#msg.add_attachment(file_data, maintype = 'image',subtype = file_type,filename = file_name)
'''


#sending map image with href link
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

 

