class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []
    
    def get_balance(self):
        return self.balance

    def get_statement(self):
        return self.transactions

    def deposit(self, amount):
        self.balance += amount