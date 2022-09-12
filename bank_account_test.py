from bank_account import *
from unittest.mock import MagicMock
from datetime import datetime


def test_initial_account():
    account = BankAccount()
    assert type(account) == BankAccount
    assert (account.get_balance()) == 0
    assert (account.get_statement()) == []


def test_depositing_100():
    account = BankAccount()
    account.deposit(100)
    mock_date = MagicMock(return_value = datetime(2022, 9, 10))
    transaction = {
        "Date": datetime(2022, 9, 10),
        "Credit": 100,
        "Debit": None,
        "Balance": 100
    }
    statement = account.get_statement()
    assert type(account) == BankAccount
    assert (account.get_balance()) == 100
    assert transaction in statement
    assert len(statement) == 1


def test_withdrawal_of_50():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(20)
    assert (account.get_balance()) == 80
