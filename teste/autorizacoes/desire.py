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

    def desire(self):
        want = str(input("Continuar? (1)Yes (2)No: ")).lower().strip()
        if want == "1" or want == "yes":
            self.autorization_wanted = True
        elif want == "2" or want == "no":
            self.autorization_wanted = False
        else:
            self.desire()