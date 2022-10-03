import sys
sys.path.append(r'./lib/utils/')
from createDashboardSettings import (settings_exists, create_settings,
                                     ConfigParser, config_file_path)


class UpdateDashboardSettings:
   
    def __init__(self) -> None:
        if not settings_exists():
            create_settings()
        self.settings = ConfigParser()
        self.settings.read(config_file_path)

    
    
    
    def set_upload(self, value) -> bool:
        self.settings.set('DEFAULT','minUploadSpeed',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)
    
    
    
    def set_download(self, value) -> bool:
        self.settings.set('DEFAULT','minDownloadSpeed',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)
    
    
    def set_recipient_email(self, value) -> bool:
        self.settings.set('DEFAULT','recipientEmail',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)
    
    
    
    def set_modem_loc(self, value) -> bool:
        self.settings.set('DEFAULT','modemLocation',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)       
    
    
    
    
    def set_sender_email(self, value) -> bool:
        self.settings.set('DEFAULT','senderEmail',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)    
    
    
    
    def set_password(self, value) -> bool:
        self.settings.set('DEFAULT','password',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)    
    
    
    def set_port(self, value) -> bool:
        self.settings.set('DEFAULT','port',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)    
    
    
    def set_server(self, value) -> bool:
        self.settings.set('DEFAULT','server',value)
        with open(config_file_path, 'w') as new_config:
            self.settings.write(new_config)   
    
    
    
    
# TODO:
# -[] Document each method