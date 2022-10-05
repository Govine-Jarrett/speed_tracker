# Check if Config file exits before the app can run.
# If not available create a config file with the following.

# 7/2/2022
from os import mkdir, path, system
from configparser import ConfigParser

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
        'isFirstTime':'True',
    }
    
    # check if path exists
    if not path.exists(config_file_path):
        mkdir('./res/config/')
    # Create and write settings to file
    with open(config_file_path, 'w') as config_file_data:
        config.write(config_file_data)
        
    # Hide config file and folder
    system(f'attrib +h ./res/config')
    system(f'attrib +h {config_file_path}')