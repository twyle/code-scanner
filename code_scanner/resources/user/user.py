class User:
    def __init__(self, username: str, email: str):
        self.__username = username
        self.__email = email
        
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email