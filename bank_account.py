import datetime


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
        date = self.__get_time()
        self.transactions.append({
            "Date": date,
            "Credit": amount,
            "Debit": None,
            "Balance": self.balance
        })

    def withdraw(self, amount):
        self.balance -= amount

    def __get_time(self):
        return datetime.datetime.now().date()
