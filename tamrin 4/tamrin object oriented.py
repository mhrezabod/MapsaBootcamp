import re

class Account:
    
    def __init__(self,username,password,phone_number,email):

        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.email = email

    @staticmethod
    def check_username (username):
        pass

    @staticmethod
    def check_password (password):
        pass

    @staticmethod
    def check_phone_number (phone_number):
        pass
    
    @staticmethod
    def check_email (email):
        pass
