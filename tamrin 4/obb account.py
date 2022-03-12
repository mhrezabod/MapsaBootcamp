import re
import hashlib

class Account:
    
    def __init__(self,username,password,phone_number,email):

        self.username = Account.check_username(username) 
        self.password = Account.check_password(password)
        self.phone_number = Account.check_phone_number(phone_number)
        self.email = Account.check_email(email)

    @staticmethod
    def check_username (username):
        if not re.search("^[a-zA-Z]+_[a-zA-Z]+$",username):
            raise "invalid username"
        return username

    @staticmethod
    def check_password (password):
        if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",password):
            raise "invalid passwrod"
        
        password = hashlib.sha256(password.encode('utf-8'))

        return password

        

    @staticmethod
    def check_phone_number (phone_number):
        if not re.search("^((\+989)|(09))+[0-3,9]\d{8}$",phone_number):
            raise "invalid Phone number" 

        if phone_number.startswith("+98"):
            phone_number = phone_number.replace('+989','09')

        return phone_number

  
    @staticmethod
    def check_email (email):
        if not re.search("[\w.-]+@[\w.-]+\.[a-zA-Z]{2,5}",email):
            raise "invalid email"
        return email

if __name__== "__main__":
    account = Account ("al_sdi",'1sd3d2dsA','+989121124066','mohammad.reza.bod@gmail.com')
    print(account.username)
    print(account.password)
    print(account.phone_number)
    print(account.email)
