"""Design a BankAccount class that represents a bank account with basic functionalities
like deposit, withdrawal, and balance check."""

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print("Deposited:",amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:",self.balance)

#Create BankAccount objects
account1=BankAccount()
account2=BankAccount()

#Deposit into account1
account1.deposit(1000)

#Withdraw
account2.withdraw(200)  #Insufficient balance
account1.withdraw(100)

#Deposit into account2
account2.deposit(1500)

#Check balance
account1.check_balance()
account2.check_balance()
