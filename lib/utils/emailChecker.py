from string import ascii_lowercase as letters 
from string import  digits 

# TODO:
# -[x] Update to not take the provider arg

def is_email_valid(email_to: str)-> bool:
    """
    Check if the email address is valid.
    """
    allowed_chars_for_name = [_ for _ in letters+digits+'.']
    allowed_chars_for_mail_provider = [_ for _ in letters+'.']
    

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
        
        # Check if the mail provider dont end with a . period
        
        if len(recipients_name) >= 5:
            name = []
            for char in recipients_name:
                if char not in allowed_chars_for_name:
                    name.append(char)
            if len(name) == 0:
                # Storing the illegal chars
                not_allowed_char = []
                # Check total @ symbol
                at_sign_count = mail_provider.count('@')

                
                # Checking for illegal chars
                index_count = 0
                for new_char in mail_provider[1:]:
                    if new_char not in allowed_chars_for_mail_provider:
                        not_allowed_char.append(new_char)
                    index_count += 1


                if len(not_allowed_char) == 0:
                    if at_sign_count == 1  and  not mail_provider[index_count:] == '.':
                        return True
                    else:
                        return False
                else:
                    return False
                
            
            
            else:
                return False
            
        else:
            return False
        # CHECKING IF THE MAIL PROVIDER IS PROVIDER - END
    
    except ValueError as event:
        return False


