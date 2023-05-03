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
        trying_password = str(
            input(f"Please type the password for {self.holder}'s account: "))
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
                    Bank.withdraw_done = True
                else:
                    print("Wrong password! Operation canceled")
                    Bank.withdraw_done = False
            else:
                print(
                    f"Operation canceled. the holder {self.holder} don't have the enough quantity of ${value}")
                Bank.withdraw_done = False
        else:
            print("Operation canceled")
            Bank.withdraw_done = False

    # Function to deposit the money
    def deposit(self, value,):
        print(
            f"Deposit of ${value} to the {self.holder}'s account. Do you want to continue?")
        deposit_yes_or_no = str(input("(1)yes (2)no "))
        deposit_yes_or_no.lower().strip()
        if deposit_yes_or_no == "1" or deposit_yes_or_no == "yes":
            self._balance += value
            print(
                f"Deposit of ${value} to the holder {self.holder} made with success")
            Bank.deposit_acceptance = True
        else:
            print("Operation cancelled")
            Bank.deposit_acceptance = False

    # Function to transfer money from one account to the other
    def transfer(self, destiny, value):
        self.withdraw(value)
        if Bank.withdraw_done == True:
            destiny.deposit(value)
            if Bank.deposit_acceptance == True:
                print("Trasferation operation completed")
            else:
                self._balance += value
                print(f"ERROR")

    # Function to show the account balance
    @property
    def extract(self):
        print(
            f"The account number {self._account_number} from the holder {self.holder} has a balance of ${self._balance}")

    # Function that shows all the information in a account
    @property
    def info(self):
        print(f"Holder: {self.holder} - Account Number: {self._account_number} - Balance: {self._balance} - Limit: {self.limit} - Bank: {self._bank_name} - Bank code: {self._bank_code} - ISPB: {self._ISPB} - Account country: {self._country}")


class Conta_do_Itau_Unibanco(Bank):
    def __init__(self, number, balance, holder, limit, password):
        super().__init__(number, balance, holder, limit, password)
        self._bank_name = "Itau Unibanco"
        self._bank_code = "341"
        self._ISPB = "60701190"
        self._country = "Brazil"
        

class Conta_do_Banco_do_Brasil(Bank):
    def __init__(self, number, balance, holder, limit, password):
        super().__init__(number, balance, holder, limit, password)
        self._bank_name = "Banco do Brasil"
        self._bank_code = "756"
        self._ISPB = "2038232"
        self._country = "Brazil"

Lucas_account = Conta_do_Itau_Unibanco(
    123456789, 557.23, "Lucas", 500, "131008")
LZs_account = Conta_do_Banco_do_Brasil(987654321, 0.0, "LZ", 50.0, "LZ123")

Lucas_account.info