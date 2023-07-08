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

    def deposit(self,value):
        print(f"Deposito de R${value} para o titular {self.holder}")
        import autorizacoes.desire as desire
        desire.Bank.desire(self)
        if self.autorization_wanted == True:
            self._balance += value
            print(f"Deposito de R${value} feito com sucesso!")
            from datetime import datetime
            time = datetime.now()
            with open("teste/textos/withdraw.txt","a") as file:
                            file.write(f"{self._type}_{self.holder} +R${value} at:{time}\n")
        else:
            print("Operacao cancelada") 
        