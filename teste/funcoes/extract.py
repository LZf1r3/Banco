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
    
    def extract(self):
        print(f"O titular {self.holder} possui uma renda de R${self._balance}")
        from datetime import datetime
        time = datetime.now()
        with open("teste/textos/withdraw.txt","a") as file:
            file.write(f"{self._type}_{self.holder} = R${self._balance} at:{time}\n")
