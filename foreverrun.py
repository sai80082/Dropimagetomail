import datetime
import time
import os
import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "sendermail@domain.com"  # change it to your  mail
Reciever_Email = "revievermail@domain.com"  # change it to  recievers mail
Password = 'password'  # change it to your account password
newMessage = EmailMessage()
newMessage['Subject'] = "Subject"  # subject of the mail
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content('body')  # text you want to be in body of the mail
try:
    while True:
        for file in os.listdir(path):
            if file.endswith(".jpg"):  # for particular Image extensions
                time.sleep(5)
                with open(file, 'rb') as f:
                    image_data = f.read()
                    image_type = imghdr.what(f.name)
                newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=file)

                # change according to your mail provider
                with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as smtp:
                    smtp.login(Sender_Email, Password)
                    smtp.send_message(newMessage)
                    # removing file after sending the mail
                os.remove(file)
                print(str(datetime.datetime.now()) + " " + file + " File Mailed") # logs
            time.sleep(120)
except KeyboardInterrupt():
    print("exiting")