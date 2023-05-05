# Lucas you have to correct the problem that if someome type the correct password one time that person can
# withdraw any amount of money.

class Bank:
    def __init__(self, number, holder, balance, limit, password):
        self.limit = limit
        self.holder = holder
        self._number = number
        self._balance = balance 
        self._password = password
        #Variables to autorize
        self.autorization = None
        self.oyon = None

    #Function to reset autorizations
    @property
    def reseting_autorizing(self):
        Bank.oyon = False
        self.autorization = False
    #Function to print the balance in a account
    @property
    def extract(self):
        print(f"The holder {self.holder} has a balance of ${self._balance}")

    #Function to verify if the password match with the original one
    @property
    def verify_password(self):
        chances = 2
        while chances >= 0:
            receiving_password = str(input(f"Please type the password for {self.holder}'s account: "))
            if receiving_password == self._password:
                self.autorization = True
                print("Right password!")
                break
            else:
                print(f"Wrong password! You have {chances} tries left.")
                chances -= 1 
        
    #Function to verify if the holder have enough money to execute the action

    def verify_balance(self, value):
        if self.limit + self._balance > value:
            self.verify_password
        else:
            print(f"Operation canceled because the holder {self.holder} don't have enough money to complete the trasation")

    #Function to confirm the Action
    @property
    def operation_yes_or_no(self):
        oyon = str(input("(1)yes (2)No "))
        oyon.strip().lower()
        if oyon == "1" or oyon == "yes":
            Bank.oyon = True
        else:
            Bank.oyon = False
#-----------------------------------------------------------------------------
#Function of Actions

    #Function for withdraw
    def withdraw(self, value):
        print(f"Withdraw in the value of ${value} in the {self.holder}'s account . Want to continue?")
        self.operation_yes_or_no
        if Bank.oyon == True:
            Bank.verify_balance(self, value)
            if self.autorization == True:
                self._balance -= value
                print(f"Withdraw of ${value} for the holder {self.holder} made with success!")
        else:
            print("Operation canceled!")

    #Function for Deposit
    def deposit(self, value):
        print(f"Deposit in the value of ${value} to the holder {self.holder}. Do you want to continue?")
        self.operation_yes_or_no
        if Bank.oyon == True:
            self._balance += value
            print(f"Deposit of ${value} to the holder {self.holder} made with success!")
        

    #Function for tranfer
    def transfer(self, destiny, value):
        print(f"Transferation of ${value} from the holder {self.holder} to the holder {destiny.holder}. Please follow the next steps:\n")
        self.withdraw(value)
        if self.autorization == True:
            destiny.deposit(value) 
            if Bank.oyon == False:
                print("Operation canceled!")
                self._balance += value
        

            

account_test_1 = Bank("xxxxxxxx", "xpto", 000.00, 999.99, "3.1415592653") 
account_test_2 = Bank("yyyyyyyy", "otpx", 999.99, 000.00, "2.7182818284")

account_test_1.transfer(account_test_2, 50)
account_test_1.extract
account_test_2.extract
account_test_1.withdraw(949.99)
account_test_1.extract