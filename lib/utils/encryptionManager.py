from os import system
from cryptography.fernet import Fernet


MASTER_KEY_FILE = './res/config/master.key'



def create_key() -> None:
    """
    Create a master key and store it in the key folder.
    """
    key = Fernet.generate_key()
    # Create and store the key into the key folder.
    with open(MASTER_KEY_FILE, 'wb') as file:
        file.write(key)
    print("Master key created.")
    # Hide the file
    system(f'attrib +h {MASTER_KEY_FILE}')
    



def read_key() -> bytes:
    """
    Reads the master key from the key folder.

    Returns:
        bytes: The key.
    """
    with open(MASTER_KEY_FILE, 'rb') as file:
        key = file.read()
    return key




def encrypt_password(key:bytes, password:str) -> bytes:
    """
    Encrypt the password before inserting into
    the database.

    Args:
        key (bytes): The master key use to encrypt and decrypt the password.
        password (str): The password that will be inserted into the database.

    Returns:
        bytes: The encrypted password.
    """
    f = Fernet(key)
    password.encode('utf-8')
    encrypted_password = f.encrypt(bytes(password, 'utf-8'))
    return encrypted_password




def decrypt_password(key:bytes, password:str) -> str:
    """
    Decrypt the password for the database.

    Args:
        key (bytes): The master key use to encrypt and decrypt the password.
        password (str): The password that was fetched from the database.

    Returns:
        str: The decrypted password.
    """
    f = Fernet(key)
    decrypted_password = f.decrypt(password).decode('utf-8')
    return decrypted_password
