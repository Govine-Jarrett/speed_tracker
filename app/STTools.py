#  This is all the tools that the app need to run.
import configparser
import os
from os import path, environ
import logging
from string import ascii_lowercase as letters
from smtplib import SMTP_SSL
from email.message import EmailMessage


config_file_path = 'setting/speedTracker.ini'
log_file_path = 'logs/'


##--------------------START Check Environment Variable --------------------##
def environ_var_exists() -> bool:
    """
    Check if the following environment variables
    below exist and is not empty.
    
    SPEED_TRACKER_EMAIL: The email which the app will use to send notifications
    SPEED_TRACKER_PWD: The password for the email.

    Returns:
        bool: True if both environment variables exist and is not empty, otherwise False. 
    """
    if os.environ.get('SPEED_TRACKER_EMAIL') != None and os.environ.get('SPEED_TRACKER_PWD') != None:
        return True
    else:
        logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path+'environVarExists.log')
        logging.warning('You need to setup the environment variables. ')
        return False

##--------------------END Check Environment Variable --------------------##


##--------------------START Check If Settings File Exists --------------------##

def settings_exists() -> bool:
    """ Check if the Speed Tracker settings file exists.
    Returns:
        bool: True is the file exists, otherwise False.
    """
    if path.exists(config_file_path):
        return True
    else:
        logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path+'createSettings.log')
        logging.warning('The settings file is not available. ')
        return False


def create_settings() -> None:
    """Create the app settings file.
    NOTE:
    Both speeds are in mega bites
    """
    
    config = configparser.ConfigParser()
    
    # Create section and settings
    config['DEFAULT'] = {
        'receiverEmail': 'example@domin.com',
        'emailProvider': '@gmail.com',
        'minDownloadSpeed': '150',
        'minUploadSpeed': '150',
        'modemLocation': 'Home Office'
    }
    
    # Create and write settings to file
    with open(config_file_path, 'w') as config_file_data:
        config.write(config_file_data)
    
    # Log this event.
    logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path+'createSettings.log')
    logging.warning('Created on: ')
    
##--------------------END Check If Settings File Exists --------------------##


##--------------------START Convert Bytes --------------------##
# The is from https://pytutorial.com/python-test-internet-speed, this not my code.
def convert_bytes(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
##--------------------END Convert Bytes --------------------##


##--------------------START Validate Email --------------------##

def email_is_valid(email_to: str, provider: str)-> bool:
    """Check if the email address is valid base on the given provider or default.
    NOTE:
    The default provider is gmail.com, this can be changed in the settings file.
    """
    
    logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path+'emailValidator.log')
    
    # ALLOWED CHARACTERS FOR THE EMAIL -START
    allowed_chars = [_ for _ in f"{letters}.0123456789"]
    # ALLOWED CHARACTERS FOR THE EMAIL -END
   
    # FORMATTING THE INPUT - START
    word = email_to.lower()
    # FORMATTING THE INPUT - END

    try:
        # GETTING THE INDEX FOR THE AT SIGN - START
        at_sign_index = word.index('@')
        # GETTING THE INDEX FOR THE AT SIGN - END
        
        # GETTING THE EMAIL PROVIDER - START
        mail_provider = word[at_sign_index:]
        # GETTING THE EMAIL PROVIDER - END

        # GETTING THE EMAIL USERS NAME - START
        recipients_name = word[:at_sign_index]
        # GETTING THE EMAIL USERS NAME - END
        
        # CHECKING IF THE MAIL PROVIDER IS PROVIDER - START
        if mail_provider == provider and len(recipients_name) >= 5:
            not_allowed_chars = []
            for char in recipients_name:
                if char not in allowed_chars:
                    not_allowed_chars.append(char)
            if len(not_allowed_chars) == 0:
                return True
            else:
                logging.warning("Something is wrong with this email. ")
                return False
        else:
            logging.warning("Please use a valid receiver's email. ")
            return False
        # CHECKING IF THE MAIL PROVIDER IS PROVIDER - END
    
    except ValueError as event:
        # Log error
        logging.warning(str(event))

##--------------------END Validate Email --------------------##



##--------------------START Sending Email --------------------##

def send_email(upload:str, download:str, ping:str, link:str, email_to: str, loc:str, email_from: str =environ.get('SPEED_TRACKER_EMAIL'), email_pwd: str =environ.get('SPEED_TRACKER_PWD') )-> None:
    """SEND GMAIL"""
    
    logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path+'emailSender.log')
    
    try:
        gmail_server = 'smtp.gmail.com'
        gmail_port = 465

        # CREATING THE EMAIL MESSAGE - START
        msg = EmailMessage()
        msg['Subject'] = 'SPEED TRACKER ALERT' # Subject of Email
        msg['From'] = "DGApps.io"
        msg['To'] = email_to
        msg.set_content(
            f'\nWARNING: Your internet speed is dropping.\n\
            \nLocation: {loc}\
            \nUpload: {upload}\
            \nDownload: {download}\
            \nPing: {ping}ms\
            \nImage: {link}\
            \n\nPlease contact Flow then report this issue to your work.\
            \nPowered by DGApps.io') # Email body or Content
        # CREATING THE EMAIL MESSAGE - END


        # SENDING EMAIL - START
        with SMTP_SSL(gmail_server, gmail_port) as smtp:
            smtp.login(email_from, email_pwd)
            smtp.send_message(msg)
            logging.info(f'Report was sent to {email_to}')
        # SENDING EMAIL - END
        
    except Exception as emailSenderError:
        logging.warning(str(emailSenderError))

##--------------------END Sending Email --------------------##