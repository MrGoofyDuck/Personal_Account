from Amount import Amount

class personal_account:
    def __init__(self, account_number, account_holder, balance, transaction):
        self.account_number = int(account_number)
        self.account_holder = str(account_holder)
        self.balance = float(balance)
        self.transactions = []
    
    def deposit (self, amount):
        transaction =  Amount( amount, 'DEPOTSIT')
        self.transactions.append(transaction)
        self.balance +=amount
        print(f"Deposit: {amount}, New Balance: {self.balance}")

    def withdraw (self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return 
        transaction = Amount(amount, "WITHDRAW")
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Withdrew: {amount}, New Balance: {self.balance}")

    def print_transaction_history(self):
        for transcation in self.transactions:
            print(f"{transcation.transaction_type}: {transcation.amount}")

    def get_balance(self):
        return self.balance

    def get_account_number (self):
        return self.account_number 
    
    def set_account_number (self, account_number ):
        return self.account_number == account_number
    
    def get_account_holder (self):
        return self.account_holder
    
    def set_account_holder(self, account_hoder):
        return self.account_holder == account_hoder
    
    def __str__ (self):
        return f"BankAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance={self.balance})"

    def __add__(self, amount):
        self.deposit(amount)
        
    def __sub__(self, amount):
        self.withdraw(amount)

