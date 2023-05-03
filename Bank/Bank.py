class Bank:
    # Setting the commom variables
    def __init__(self, number, balance, holder, limit, password):
        self._account_number = number
        self._balance = balance
        self.holder = holder
        self.limit = limit
        self._password = password
        self.autorization = None
        self.withdraw_done = None
        self.deposit_acceptance = None

    # Function to verify if the password is correct
    def _verify_password(self):
        trying_password = str(input(f"Please type the password for {self.holder}'s account: "))
        if trying_password == self._password:
            self.autorization = True

        else:
            self.autorization = False


    # Function to withddraw the money
    def withdraw(self, value):
        print(f"Withdraw of ${value}. Do you want to continue?")
        withdraw_yes_or_no = str(input("(1)yes (2)no "))
        withdraw_yes_or_no.lower().strip()
        if withdraw_yes_or_no == "1" or withdraw_yes_or_no == "yes":
            if self._balance + self.limit > value:
                Bank._verify_password(self)
                if self.autorization == True:
                    self._balance -= value
                    print("Operation accepted")
                    self.withdraw_done = True
                else:
                    print("Wrong password! Operation canceled")
                    self.withdraw_done = False
            else:
                print(f"Operation canceled. the holder {self.holder} don't have the enough quantity of ${value}")
                self.withdraw_done = False
        else:
            print("Operation canceled")
            self.withdraw_done = False

    #Function to deposit the money
    def deposit(self, value,):
        print(f"Deposit of ${value} in the {self.holder}'s account. Do you want to continue?")
        deposit_yes_or_no = str(input("(1)yes (2)no "))
        deposit_yes_or_no.lower().strip()
        if deposit_yes_or_no == "1" or deposit_yes_or_no == "yes":
            self._balance += value
            print(f"Deposit of ${value} to the holder {self.holder} made with success")
            self.deposit_acceptance = True
        else:
            print("Operation cancelled")
            self.deposit_acceptance = False

    #Function to transfer
    def transfer(self, destiny, value):
        self.withdraw(value)
        if self.withdraw_done == True:
            destiny.deposit(value)
            if self.deposit_acceptance == True:
                print("Operation completed")
            else:
                self._balance += value
                print(f"ERROR")
        
        

    #Function to show the account balance
    @property
    def extract(self):
        print(f"The account number {self._account_number} from the holder {self.holder} has a balance of ${self._balance}")

class Conta_do_Itau_Unibanco(Bank):
    def __init__(self, number, balance, holder, limit, password):
        super().__init__(number, balance, holder, limit, password)
        self.__bank_name = "Itau Unibanco"
        self.__bank_code = "xxx"


Lucas_account = Conta_do_Itau_Unibanco(123456789, 557.23, "Lucas", 500, "131008")
LZs_account   = Conta_do_Itau_Unibanco(987654321, 0.0, "LZ", 50.0, "LZ123")
Lucas_account.transfer(LZs_account, 50)
print(Lucas_account._balance)
print(LZs_account._balance)
