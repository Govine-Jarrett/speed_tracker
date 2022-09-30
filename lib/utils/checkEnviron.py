# Check if the environment variable exist before the app can run.
# If not show a popup dialog to the user, to let them create the
# following var SPEED_TRACKER_EMAIL and SPEED_TRACKER_PWD
# 7/2/2022
import os


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

