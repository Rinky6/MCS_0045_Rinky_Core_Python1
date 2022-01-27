import  os
import smtplib
from email.message  import EmailMessage
def solution():
    # file = ['sample.pdf']
    with open('sample.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype ='application',subtype = 'octet-stream' , filename = file_name )
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

        smtp.login(mail_id,input("Enter password : "))

        #subject = "Checking"
        #body = "Done"
        #msg = f'Subject : {subject}\n\n{body}'
        smtp.send_message(msg)

mail_id = input("Enter email ")
msg = EmailMessage()
msg['Subject'] ="Checking"
msg['From']= mail_id
msg['To'] = 'rinkykum4444@gmail.com'
msg.set_content("  PFA below..... ")

solution()