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

    def password_verifier(self):
        chances = 2
        while chances >= 0:
            receiving_password = str(input(f"Por favor digite a senha para a conta de {self.holder}: "))
            if receiving_password == self._password:
                self.autorization_password = True
                print("Senha correta!")
                break
            else:
                print(f"Senha errada! {chances} tentativas restantes.")
                self.autorization_password = False
                chances -= 1 