class BankAccount:
    def __init__(self, banking_id, customer_name, BSB, balance=0):
        self.banking_id = banking_id
        self.customer_name = customer_name
        self.BSB = BSB
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Transaction complete. Balance: {self.balance}"
        else:
            return f"Invalid Transaction. Try again!"
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawl successful! Balance: {self.balance}"
        else:
            # In case of error, check this line and line 12. In other examples, this line did not have "f" in the statement. Not sure why
            return f"Invalid transaction. Insufficient funds or wrong"
        
    def check_balance(self):
        return f"Balance available: {self.balance}"

# Create a bank account for Gummy with an initial balance of $500,000    
gummy_account = BankAccount(42599620, "gummy", 650070, 500000)

# Check balance
print(gummy_account.check_balance())

# Deposit money
print(gummy_account.deposit(20000))

# Check balance again
print(gummy_account.check_balance())

# Withdraw money
print(gummy_account.withdraw(2000))

# Withdraw more money than balance
print(gummy_account.withdraw(520000))