from datetime import datetime 
class Amount:

    def __init__(self, amount, transaction_type):
        self.amount = float(amount)
        self.transaction_type = transaction_type

    def __str__(self):
        return print(f"Amount: {self.amount},Timestamp: {datetime.now()},Transsaction_type: {self.transaction_type}")

    