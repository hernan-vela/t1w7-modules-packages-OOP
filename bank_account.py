class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit Successful! New Balance: {self.balance}"
        else:
            return f"Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful! New balance: {self.balance}"
        else:
            return f"Invalid withdrawal amount or insufficient funds!"
    
    def get_balance(self):
        return f"Account Balance: {self.balance}"


# Create a bank account for John with an inital balance of 1000
john_account = BankAccount("John", 1000)

# Check balance
print(john_account.get_balance())

# Deposit money
print(john_account.deposit(500))

# Check balance again
print(john_account.get balance())

# Withdraw money
print(john_account.withdraw(200))

#Withdraw more money than the balance
print(john_account.withdraw(2000))