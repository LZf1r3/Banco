class Bank:
    def __init__(self, number, holder, balance, password, type):
        self.limit = balance + balance*2
        self.holder = holder
        self._number = number
        self._balance = balance 
        self._password = password
        self._type = type

        #Variables to autorize
        self.autorization_password = None
        self.autorization_balance = None
        self.autorization_wanted = None
    
    def reseting_autorizations(self):
        self.autorization_balance == None
        self.autorization_password == None
        self.autorization_wanted == None
