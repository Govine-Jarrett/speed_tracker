import sys
sys.path.append(r'./lib/utils/')
from encryptionManager import decrypt_password, read_key, encrypt_password
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
        return int(self.settings['DEFAULT']['minUploadSpeed'])
    
    
    
    def get_download(self) -> int:
        """
        Get the minimum download speed for the config file.

        Returns:
            int: The pre-define speed in MB
        """
        return int(self.settings['DEFAULT']['minDownloadSpeed'])
    
    
    
    
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
        store_pwd = self.settings['DEFAULT']['password']
        # is_first = self.get_status()
        is_first = True
        if not is_first:
            return decrypt_password(read_key(), store_pwd)
        else:
            return  store_pwd

        # TODO: need to work on
    
    
    
    def get_port(self) -> int:
        """
        get a pre-define SMTP server port from the config file.
        
        Returns:
            int: The pre-define port
        """
        return int(self.settings['DEFAULT']['port'])
    
    
    
    def get_server(self) -> str:
        """
        get a pre-define SMTP server from the config file.
        
        Returns:
            str: The pre-define server
        """
        return self.settings['DEFAULT']['server']
    
    
    
    
    
    def get_status(self) -> bool:
        """
        Get the current status if dashboard is been used for the first time or not.
        Returns:
            bool: return true if dashboard is launched for the first time
        """
        is_first = self.settings['DEFAULT']['isFirstTime']
        if is_first == 'True':
            return True
        # Else
        return False

        
    
    


    
# encrypted_password = ReadDashboardSettings()
# a = encrypted_password.get_password()
# print(type(a))


# password = decrypt_password(read_key(), a)
# print(password)
# encrypted_password = b'gAAAAABjPb5tkubFc5MLOPB4uvPRClhHDNU6zNXvKTV2g4LS2dlZN2zjR68cWUcaHvyhkzM1Wc5hNl5hlIChTIZSueeVT3HGjA=='
# print(f'ENCRYPTED: {encrypted_password}')


# decrypted_password = a
# print(f'DECRYPTED: {decrypt_password(read_key(), decrypted_password)}')
# BUG
# [] issues decrypting the password