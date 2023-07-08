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

#Withdraw
    def withdraw(self, value):
        import funcoes.withdraw as withdraw
        withdraw.Bank.withdraw(self, value)
        repetir()

#Deposit
    def deposit(self, value):
        import funcoes.deposit as deposit
        deposit.Bank.deposit(self,value)
        repetir()

#Printing the extract
    @property
    def extract(self):
        import funcoes.extract as extract
        extract.Bank.extract(self)
        repetir()

Lucas_account = Bank('013102008', "Lucas Faiad", 1000, "131008", "cc")

############################################
# Code for login page

def historico():
    import secundarios.historic as historic
    historic.historic()

def verificando_conta():
    pass
        
def o_que_fazer():
    oqf = str(input("O que deseja fazer? "))
    if oqf == "saque":
        valor = float(input("Digite o valor do saque: R$"))
        Lucas_account.withdraw(valor)
    elif oqf == "deposito":
        valor = float(input("Digite o valor do deposito: R$"))
        Lucas_account.deposit(valor)
    elif oqf == "extrato":
        Lucas_account.extract
    elif oqf == "transferencia":
        destino = str(input("Digite o codigo de destino do destinatario: "))
        valor = float(input("Digite o valor da transferencia: R$"))
        pass
    elif oqf == "historico":
        historico()
    else:
        programadores = ["Lucas Faiad: +55 49 99162 1223", "LZ: +55 48 99162 1223", "xpto: +55 48 99162 1223"]
        print("Funcao nao encontrada! Contate um dos programadores:")
        for programador in programadores:
            print(programador)

def repetir():
    repetir = str(input("Continuar utilizando o banco-LZ? (1)Yes (2)No ")).lower()
    o_que_fazer() if repetir == "1" or repetir == "no" else print("Programa encerrado!\n    Made By LZ.")
if __name__ == "__main__":
    o_que_fazer()