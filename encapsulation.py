class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Public methods to access and modify private attributes
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

# Create a BankAccount object
account = BankAccount("123456789", 1000)

# Access and modify private attributes using public methods
print(account.get_account_number())  # Output: 123456789
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Attempt to access private attributes directly leads to error
print(account.__account_number)  # Error: AttributeError