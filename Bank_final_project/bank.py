from datetime import datetime
time = datetime.now()
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

#Reseting autorizations
    @property
    def reseting_autorizations(self):
        self.autorization_balance == None
        self.autorization_password == None
        self.autorization_wanted == None

#Verifying password
    @property
    def verify_password(self):
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

#Verifying balance
    def verify_balance(self, value):
        if value > self._balance + self.limit:
            self.autorization_balance = False
        else:
            self.autorization_balance = True

#Verifying desire
    @property
    def verify_desire(self):
        want = str(input("Continuar? (1)Yes (2)No: ")).lower().strip()
        if want == "1" or want == "yes":
            self.autorization_wanted = True
        elif want == "2" or want == "no":
            self.autorization_wanted = False
        else:
            self.verify_desire

#Withdraw
    def withdraw(self, value):
        print(f"Saque da conta de {self.holder} no valor de R${value}")
        self.verify_desire
        if self.autorization_wanted == True:
            self.verify_balance(value)
            if self.autorization_balance == True:
                self.verify_password
                if self.autorization_password == True:
                    self._balance -= value
                    print(f"Saque de R${value} foi feito com sucesso!")
                    with open("Bank_final_project/usos.txt","a") as file:
                        file.write(f"{self._type}_{self.holder} -R${value} at:{time}\n")
                else:
                    print("Operacao cancelada devido a multiplas tentativas de senha!")
            else:
                print(f"Operacao cancelada pois o titular {self.holder} nao possui dinheiro suficiente!")
        else:
            print("Operacao cancelada!")
        self.reseting_autorizations
        repetir()

#Deposit
    def deposit(self, value):
        print(f"Deposito de R${value} para o titular {self.holder}")
        self.verify_desire
        if self.autorization_wanted == True:
            self._balance += value
            print(f"Deposito de R${value} feito com sucesso!")
            with open("Bank_final_project/usos.txt","a") as file:
                        file.write(f"{self._type}_{self.holder} +R${value} at:{time}\n")
        else:
            print("Operacao cancelada") 
        repetir()

#Printing the extract
    @property
    def extract(self):
        print(f"O titular {self.holder} possui uma renda de R${self._balance}")
        with open("Bank_final_project/usos.txt","a") as file:
                        file.write(f"{self._type}_{self.holder} = R${self._balance} at:{time}\n")
        repetir()

Lucas_account = Bank('013102008', "Lucas Faiad", 1000, "131008", "cc")

############################################
# Code for login page

def historico():
    with open("Bank_final_project/usos.txt","r") as usos:
        for linha in usos:
            print(linha)

def verificando_conta():
    conta_num = str(input("Digite o numero da sua conta: "))
    if conta_num == "cancel":
        print("Programa encerrado!\n   Made By LZ.")
        exit()
    conta_tit = str(input("Digite o nome do titular da sua conta: "))
    if conta_num == Lucas_account._number and conta_tit == Lucas_account.holder:
        print("Logged como Lucas Faiad!")
        o_que_fazer()
    else:
        print("Conta nao encontrada! Tente novamente ou digite 'cancel' para encerrar o programa.")
        verificando_conta()
        


        
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
    print("You are not supposed to do it!\n !!!Please open the login code first and execute from there!!!")