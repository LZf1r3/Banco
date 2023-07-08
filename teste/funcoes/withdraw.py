
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
        
    def withdraw(self, value):
            print(f"Saque da conta de {self.holder} no valor de R${value}")
            import autorizacoes.desire as desire
            desire.Bank.desire(self)
            if self.autorization_wanted == True:
                import autorizacoes.balance as balance
                balance.Bank.balance_check(self,value)
                if self.autorization_balance == True:
                    import autorizacoes.password as password
                    password.Bank.password_verifier(self)
                    if self.autorization_password == True:
                        from datetime import datetime
                        time = datetime.now()
                        self._balance -= value
                        print(f"Saque de R${value} foi feito com sucesso!")
                        with open("teste/textos/withdraw.txt","a") as file:
                            file.write(f"{self._type}_{self.holder} -R${value} at:{time}\n")
                    else:
                        print("Operacao cancelada devido a multiplas tentativas de senha!")
                else:
                    print(f"Operacao cancelada pois o titular {self.holder} nao possui dinheiro suficiente!")
            else:
                print("Operacao cancelada!")
            import autorizacoes.reseting_autorizations as reseting_autorizations
            reseting_autorizations.Bank.reseting_autorizations(self)

            
