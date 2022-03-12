
class Site:
    def __init__(self,url):
        self.url=url
        self.register_users=[]
        self.active_users=[]
    
    def register(self,user):

        if user in self.register_users:
            raise Exception ("user already registered")
        else:
            self.register_users.append(user)
            print("register successful")
    
    def login(self):
