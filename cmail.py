import smtplib
from smtplib import SMTP
from email.message import EmailMessage

def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sairajumantipally1328@gmail.com',"iubs lecr vtzv wype")
    msg=EmailMessage()
    msg['From ']='sairajumantipally1328@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()



