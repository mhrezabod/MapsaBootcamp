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
            raise Exception ("invalid username")
        return username

    @staticmethod
    def check_password (password):
        if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",password):
            raise Exception ("invalid password")
        
        password = hashlib.sha256(password.encode('utf-8'))

        return password

        

    @staticmethod
    def check_phone_number (phone_number):
        if not re.search("^((\+989)|(09))+[0-3,9]\d{8}$",phone_number):
            raise Exception ("invalid phone number") 

        if phone_number.startswith("+98"):
            phone_number = phone_number.replace('+989','09')

        return phone_number

  
    @staticmethod
    def check_email (email):
        if not re.search("[\w.-]+@[\w.-]+\.[a-zA-Z]{2,5}",email):
            raise Exception ("invalid email")
        return email

# if __name__== "__main__":
#     account = Account ("al_sdi",'1sd3d2dsA','+989112124066','mohammad.reza.bod@gmail.com')
#     print(account.username)
#     print(account.password)
#     print(account.phone_number)
#     print(account.email)

user = Account('mmdo_sein', 'salamM22', '09120334489', 'mh.r9776@gmail.com')
class Site:
    def __init__(self,url):
        #self.user = user
        self.url = url
        self.register_user = []
        self.active_user = []
    
    def register(self ,user):
        if user in self.register_user:
            raise Exception('user already registered')
        else:
            self.register_user.append(user)
            print("registred succesesfully")

    def _login(self, **kwdict):
        if 'password' not in kwdict:
            return 'invalid login'
        else:
            hashpass = hashlib.sha256(kwdict['password'].encode('utf-8')).hexdigest()
            
        if all(a in kwdict for a in 'username email'.split()):
            for user in self.register_user:
                if user.username == kwdict['username'] and user.email == kwdict['email'] and user.password == hashpass:
                    self.active_user.append(user)
                    return "login successfully"
                    
        elif 'username' in kwdict:
            for user in self.register_user:
                if user.username == kwdict['username'] and user.password == hashpass:
                    self.active_user.append(user)
                    return "login successfully"
                
        elif 'email' in kwdict:
            for user in self.register_user:
                if user.email == email and user.password == hashlib.sha256(password.encode('utf-8')):
                    self.active_user.append(user)
                    return "login successfully"   
                
        return 'invalid login'
    
    def _check_active(self, **kwdict):
        if 'username' in kwdict:
            for user in self.active_user:
                if user.username == kwdict['username']:
                    return 'user already loged in'
        elif 'email' in kwdict:
            for user in self.active_user:
                if user.email == kwdict['email']:
                    return 'user already loged in'
        return None
    
    def login(self, **kwdict):
        active = self._check_active(**kwdict)
        if active is None:
            active = self._login(**kwdict)
        return active
        
            
    def logout(self, user):
        if user in self.active_user:
            self.active_user.remove(user)
            print(f"{user} logged out successfully")
        else:
            print(f"{user} is not logged in")
