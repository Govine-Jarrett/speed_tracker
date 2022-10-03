class EmailServers:
    def __init__(self) -> None:
        pass
    
    
    
    def get_ports(self) -> list:
        """
        Returns a list of SMTP server ports.

        Returns:
            list: list of ports
        """
        return ['995', '587' ,'465' ,'110' ,'25']
    
    
    def get_servers(self) -> list:
        """
        Returns a list of SMTP servers.

        Args:
            list: list of servers
        """
        servers = [
            'smtp.gmail.com',
            'smtp.live.com',
            'smtp.office365.com', 
            'smtp.mail.yahoo.com' ,
            'smtp.mail.yahoo.co.uk',
            'smtp.mail.yahoo.com',
            'smtp.o2.ie',
            'smtp.o2.co.uk',
            'smtp.aol.com',
            'smtp.att.yahoo.com',
            'smtp.ntlworld.com',
            'pop3.btconnect.com',
            'mail.btopenworld.com',
            'mail.btinternet.com',
            'smtp.orange.net',
            'smtp.orange.co.uk',
 
        ]
        return servers
    
    # TODO:
    # -[] Create a method to map ports with servers
    # -[] Add more severs from the 'list_of_servers' file