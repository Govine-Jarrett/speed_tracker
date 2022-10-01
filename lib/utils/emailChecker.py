from string import ascii_lowercase as letters
from configparser import ConfigParser
import logging
from checkSettings import config_file_path

log_file_path = 'emailChecker.log'
app_settings = ConfigParser()
app_settings.read(config_file_path)

email_provider = app_settings['DEFAULT']['emailProvider']


# TODO:
# -[] Update to not take the provider arg

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
