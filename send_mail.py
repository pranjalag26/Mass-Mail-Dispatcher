import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email_read import get_csv_data
from make_template import read_template


message_template = read_template()


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("theextradrive665@gmail.com", "Atarax665$")


def send_email(emails):
    try:
        for e in emails:
            msg = MIMEMultipart()
            message = message_template.substitute(
                EMAIL=e.title())
            msg['From'] = 'Abhinav'
            msg['To'] = e
            msg['Subject'] = "Automated Test mail "
            msg.attach(MIMEText(message, 'plain'))
            print("Mail sent to ", e)
            s.send_message(msg)

            del msg
    except:
        print("Mail Not sent to ", e)
