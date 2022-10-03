# Check if Config file exits before the app can run.
# If not available create a config file with the following.
# SECTION: STSettings
# SETTINGS: email , minDownloadSpeed, minUploadSpeed
# 7/2/2022
from os import path
from configparser import ConfigParser
# import logging

config_file_path = './res/config/dashboard.ini'

def settings_exists() -> bool:
    """ Check if the Speed Tracker settings file exists.
    Returns:
        bool: True is the file exists, otherwise False.
    """
    if path.exists(config_file_path):
        return True
    return False


def create_settings() -> None:
    """
    Create the app settings file.
    """
    
    config = ConfigParser()
    
    # Create section and settings
    # Both speeds are in MB
    config['DEFAULT'] = {
        'minUploadSpeed': '150',
        'minDownloadSpeed': '150',
        'recipientEmail': 'example@domin.com',
        'modemLocation': 'Home Office',
        'senderEmail':'speed.tracker@gmail.com',
        'password':'Password123',
        'port':'465',
        'server':'smtp.gmail.com',
    }

    # Create and write settings to file
    with open(config_file_path, 'w') as config_file_data:
        config.write(config_file_data)
    
    # # Log this event.
    # logging.basicConfig(format='%(message)s %(asctime)s', filename=log_file_path)
    # logging.warning('Created on: ')
    


# if settings_exists():
#     print('file exists.')
# else:
#     create_settings()
#     print('file created')