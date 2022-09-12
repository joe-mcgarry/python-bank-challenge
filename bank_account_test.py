from bank_account import *
import unittest

def test_initial_account():
    account = BankAccount()
    assert type(account) == BankAccount
    assert(account.get_balance()) == 0
    assert(account.get_statement()) == []
