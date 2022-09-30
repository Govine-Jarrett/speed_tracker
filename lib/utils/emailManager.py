# Manage all the email sending to different email providers, 
# but currently in version one is only supports gmail clients.
# 7/4/2022
from configparser import ConfigParser
from email.message import EmailMessage
from os import environ
from smtplib import SMTP_SSL

config_file_path = 'setting/speedTracker.ini'
log_file_path = 'logs/'

app_settings = ConfigParser()
app_settings.read(config_file_path)

test_ds = '149.76Mbps'
test_us = '131.31Mbps'
test_ping = '1ms'
test_link = 'http://www.speedtest.net/result/13359052207.png'

# receiver_email = app_settings['DEFAULT']['receiverEmail']
receiver_email = 'svgamesresults@gmail.com'
modem_loc = app_settings['DEFAULT']['modemLocation']


def send_email(email_to: str=receiver_email, email_from: str =environ.get('SPEED_TRACKER_EMAIL'), email_pwd: str =environ.get('SPEED_TRACKER_PWD') )-> None:
    """SEND GMAIL"""

    gmail_server = 'smtp.gmail.com'
    gmail_port = 465

    # CREATING THE EMAIL MESSAGE - START
    msg = EmailMessage()
    msg['Subject'] = 'SPEED TRACKER ALERT' # Subject of Email
    msg['From'] = "DGApps.io"
    msg['To'] = email_to
    msg.set_content(
        f'Your Internet Speed Is Dropping\n\
        \nLocation: {modem_loc}\
        \nUpload: {test_us}\
        \nDownload: {test_ds}\
        \nPing: {test_ping}\
        \nImage: {test_link}\
        \n\nPlease contact Flow then report this issue to your work.\
        \nPowered by DGApps.io') # Email body or Content
    
    # CREATING THE EMAIL MESSAGE - END


    # SENDING EMAIL - START
    with SMTP_SSL(gmail_server, gmail_port) as smtp:
        smtp.login(email_from, email_pwd)
        smtp.send_message(msg)
        print(f"Email sent to: {email_to}")
    # SENDING EMAIL - END


# send_email()