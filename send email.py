import smtplib
from email.message import EmailMessage

email = EmailMessage()

email["from"] = "kishore kumar"
email['to'] = "kishorekumarkp2000_me@mepcoeng.ac.in"
email['subject'] = 'you r genius sir!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com' , port=465) as smtp:
    smtp.ehlo()
    smtp.starttls          #encrytion method - connect to server protocal
    smtp.login("kishorekumarkp2000@gmail.com" , "bujima#1")
    smtp.send_message(email)
    print("all good")