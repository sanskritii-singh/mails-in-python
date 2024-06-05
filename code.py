import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Sanskriti Singh'
recipients=['sanskritisingh.inn@gmail.com']
email['to']=",".join(recipients)
email['subject']='Congratulations'
email.set_content(html.substitute({'name':"bestie"}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your email id','your password/authentication code')
    smtp.send_message(email)
    print("all good boss!") 
