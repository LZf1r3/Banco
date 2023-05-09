class Bank:
    def __init__(self, number, holder, balance, limit, password):
        self.number = number
        self.holder = holder
        self._balance = balance
        self.limit = limit
        self._password = password
        self.autorization = None

    #Function of checking password 
    @property
    def checking_password(self):
        tries = 3
        while tries > 0:
            checking_password = str(input(f"Please type the password for the holder {self.holder}: "))
            if checking_password == self._password:
                self.autorization = True
                break
            else:
                self.autorization = False
                print("Wrong password! Please try again!")
                tries -= 1


    #Function of checking balance
    def checking_balance(self, value):
        balance_check = value < self._balance + self.limit
        if balance_check:
            self.checking_password
        else:
            print(f"The holder {self.holder} doesn't have enough money.")

    #Function for extract
    @property
    def extract(self):
        print(f"The holder {self.holder} has a balance of ${self._balance}.")

    #Functions for withdraw
    def print_withdraw(self, value):
        print(f"Withdraw of ${value} for the holder {self.holder} done with success!")
    
    def exec_withdraw(self,value):
        Bank.checking_balance(self, value)
        if self.autorization == True:
            self._balance -= value

    def withdraw(self,value):
        self.exec_withdraw(value)
        if self.autorization == True:
            self.print_withdraw(value)

    #Functions for deposit
    def print_deposit(self, value):
        print(f"Deposit of ${value} to the holder {self.holder} was made with success!")
    def deposit(self, value):
        self._balance += value
    
    #Functions for transferation
    def exec_transfer(self, destiny, value):
        self.exec_withdraw(value)
        destiny.deposit(value)
    
    def print_transfer(self, destiny, value):
        print(f"Trasferation of ${value} from the holder {self.holder} to the holder {destiny.holder} was made with success!")

    def transfer(self, destiny, value):
        self.exec_transfer(destiny, value)
        self.print_transfer(destiny, value)

Lucas_account = Bank(131008, "Lucas", 500.0, 50.0, "2008")
Karol_account = Bank(202200141, "Karol", 900.00, 150.0, "0141")
Alex_account  = Bank(666666666, "Alex", 11000.0, 1000.0, "AlexAndLucas")

