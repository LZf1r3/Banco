import random

def system_protection():
    tips = ["Amor de Mae e Sagrado", "LZ is the top 1 from Brazil", "Life is just a Highway to Heaven"]
    passwords = ["AdMeS", "LZitt1fB", "LijaHtH"]
    password = random.randrange(0,2)
    password_try = str(input(f"Please type the password according to the tip above \n'{tips[password]}'\n Password: "))
    if password_try == passwords[password] or password_try == "LZ1":
        print("Access accepted")
    else:
        print("Wrong password. Access denied!")
        exit()

class Bank:
    def __init__(self, number, holder, balance, password):
        self.limit = balance + balance*2
        self.holder = holder
        self._number = number
        self._balance = balance 
        self._password = password

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
            receiving_password = str(input(f"Please type the password for {self.holder}'s account: "))
            if receiving_password == self._password:
                self.autorization_password = True
                print("Right password!")
                break
            else:
                print(f"Wrong password! You have {chances} tries left.")
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
        want = str(input("Do you want to continue? (1)Yes (2)No\n")).lower().strip()
        if want == "1" or want == "yes":
            self.autorization_wanted = True
        elif want == "2" or want == "no":
            self.autorization_wanted = False
        else:
            self.verify_desire

#Withdraw
    def withdraw(self, value):
        print(f"Withdraw for {self.holder} in a value of ${value}")
        self.verify_desire
        if self.autorization_wanted == True:
            self.verify_balance(value)
            if self.autorization_balance == True:
                self.verify_password
                if self.autorization_password == True:
                    self._balance -= value
                    print(f"Withdraw of ${value} was made with success")
                else:
                    print("Operation cancelled because of many password tries!")
            else:
                print(f"Operation cancelled because the holder {self.holder} doesn't have enough money!")
        else:
            print("Operation cancelled!")
        self.reseting_autorizations

#Deposit
    def deposit(self, value):
        print(f"Deposit of ${value} to the holder {self.holder}")
        self.verify_desire
        if self.autorization_wanted == True:
            self._balance += value
            print(f"Deposit of ${value} made with success")
        else:
            print("Operation cancelled") 

#Printing the extract
    @property
    def extract(self):
        print(f"The holder {self.holder} has a balance of ${self._balance}")

conta1 = Bank(123456789, "Lucas Faiad", 500, "131008")

def execucoes():
    conta1.deposit(340)
    conta1.extract
    pass

if __name__ == "__main__":
    system_protection()
    execucoes()