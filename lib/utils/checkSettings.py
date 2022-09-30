# Check if Config file exits before the app can run.
# If not available create a config file with the following.
# SECTION: STSettings
# SETTINGS: email , minDownloadSpeed, minUploadSpeed
# 7/2/2022
from os import path
import configparser
import logging

config_file_path = 'setting/speedTracker.ini'
log_file_path = 'logs/createSettings.log'

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
    


if settings_exists():
    print('file exists.')
else:
    create_settings()
    print('file created')