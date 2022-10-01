import sys
sys.path.append(r'./lib/utils/')
from createDashboardSettings import (settings_exists, create_settings,
                                     ConfigParser, config_file_path)


class ReadDashboardSettings:
   
    def __init__(self) -> None:
        if not settings_exists():
            create_settings()
        self.settings = ConfigParser()
        self.settings.read(config_file_path)

    
    
    
    def get_upload(self) -> int:
        """
        Get the minimum upload speed for the config file.

        Returns:
            int: The pre-define speed in MB
        """
        return self.settings['DEFAULT']['minUploadSpeed']
    
    
    
    def get_download(self) -> int:
        """
        Get the minimum download speed for the config file.

        Returns:
            int: The pre-define speed in MB
        """
        return self.settings['DEFAULT']['minDownloadSpeed']
    
    
    
    
    def get_recipient_email(self) -> str:
        """
        Get the recipient's email from the config file.
        Returns:
            str: The per-define recipient's email
        """
        return self.settings['DEFAULT']['recipientEmail']

    
    
    
    
    def get_modem_loc(self) -> str:
        """
        Get the modem location from the config file.

        Returns:
            str: The per-define location
        """
        return self.settings['DEFAULT']['modemLocation']
        
    
    
    
    
    def get_sender_email(self) -> str:
        """
        Get the sender's email from the config file.

        Returns:
            str: The per-define sender's email
        """
        return self.settings['DEFAULT']['senderEmail']
    
    
    
    
    def get_password(self) -> str:
        """
        get the recipient's password from the config file.

        Returns:
            str: The per-define password
        """
        return self.settings['DEFAULT']['password']
        
    
    
    
    
    
