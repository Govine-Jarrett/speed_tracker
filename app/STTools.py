#  This is all the tools that the app need to run.
import os
from os import path
import configparser
import logging
from string import ascii_lowercase as letters
from configparser import ConfigParser


config_file_path = 'setting/speedTracker.ini'
log_file_path = 'logs/createSettings.log'
log_file_path = 'logs/emailChecker.log'

app_settings = ConfigParser()
app_settings.read(config_file_path)

email_provider = app_settings['DEFAULT']['emailProvider']
min_ds = app_settings['DEFAULT']['minDownloadSpeed']
min_us = app_settings['DEFAULT']['minUploadSpeed']
receiver_email = app_settings['DEFAULT']['receiverEmail']
modem_loc = app_settings['DEFAULT']['modemLocation']


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
    logging.basicConfig(format='%(message)s %(asctime)s', filename=log_file_path)
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

def email_is_valid(email_to: str, provider: str = email_provider )-> bool:
    """Check if the email address is valid base on the given provider or default.
    NOTE:
    The default provider is gmail.com, this can be changed in the settings file.
    """
    allowed_chars = [_ for _ in f"{letters}.0123456789"]
   
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
            name = []
            for char in recipients_name:
                if char not in allowed_chars:
                    name.append(char)
            if len(name) == 0:
                return True
            else:
                return False
        else:
            return False
        # CHECKING IF THE MAIL PROVIDER IS PROVIDER - END
    
    except ValueError as event:
        # Log error
        logging.basicConfig(format='%(message)s %(asctime)s ', filename=log_file_path)
        logging.warning(str(event))

##--------------------END Validate Email --------------------##