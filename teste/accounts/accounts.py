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

def accounts(accounts):
    Lucas = Bank("13102008", "Lucas Faiad", 500, "131008", "cc")
    Julio = Bank("1991991", "Julio Faiad", 900, "000000000","cc")
    xpto = Bank("12345", "Larissa Faiad", 999, "larissa", "cc")
    accounts = [Lucas,Julio,xpto]
    account_write = accounts[len(accounts)-1]
    writing = f"Holder:{account_write.holder} Number:{account_write._number} Balance:{account_write._balance} Password:{account_write._password} Type:{account_write._type}"
    with open("teste/accounts/accounts.txt","r") as file:
        if writing in file.read():
            print("Conta ja registrada")
        else:
            with open("teste/accounts/accounts.txt","a+") as file:
                file.write(f"{writing}\n")
