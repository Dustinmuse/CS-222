# does not follow SRP Single responsibility (ideal way of doing it but most people don't use it)
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def createUserAccount(self):
        pass

    #follows SRP for above ^ (it just creates accounts)
    #when you add the resetPassword and sendEmail method it doesn't follow SRP anymore
    def resetPassword(self):
        pass

    def sendEmail(self):
        pass

class UserAccount: #SRP
    def __init__(self, username, password):
        self.username = username
        self.password = password

class CreateUser: #SRP
    def createUserAccount(self, username):
        pass

class PasswordReset: #SRP
    def resetPassword(self, username):
        pass

class NotifyUser: #SRP
    def sendEmail(self, username):
        pass