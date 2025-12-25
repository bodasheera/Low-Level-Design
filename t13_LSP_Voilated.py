"""
+-------------------+
|      Client       |
+-------------------+
| - accounts : List<Account> |
+-------------------+
|                   |
|                   |
+-------------------+
          |
          | 1
          |-----------------* has-a relationship (simple association)
          |
          ↓ 
+-------------------+
| <<abstract>>      |
|     Account       |
+-------------------+
| - accountNo       |
| - balance         |
+-------------------+
| + deposit(amount) |
| + withdraw(amount)|
+-------------------+
      ▲        ▲        ▲
      |        |        |   inheritance (is -a )
+-----------+ +------------+ +------------------+
|  Savings  | |  Current   | | FixedDeposit(FD) |
+-----------+ +------------+ +------------------+
"""

from abc import ABC , abstractmethod
from typing import List


class Account:

    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    @abstractmethod
    def deposit(self, amount): ...

    @abstractmethod
    def withdraw(self, amount): ...

    @property
    def balance(self):
        return self._balance   

    @property
    def account_number(self):
        return self._account_number

class SavingsAC(Account):

    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        self._balance = self.balance + amount
        print(f"New balance after deposit {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self._balance = self.balance - amount
            print(f"New balance after withdrawal {self.balance}")

        else:
            print("Insufficient balance to withdraw")

class CurrentAC(Account):

    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        self._balance = self.balance + amount
        print(f"New balance after deposit {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self._balance = self.balance - amount
            print(f"New balance after withdrawal {self.balance}")

        else:
            print("Insufficient balance to withdraw")


class FDAC(Account):

    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        self._balance = self.balance + amount
        print(f"New balance after deposit {self.balance}")

    def withdraw(self, amount):
        raise Exception("Withdrawal not allowed for Fixed Deposit Account")
    

class Client:

    def __init__(self, accounts: List[Account]):
        self._accounts = accounts

    @property
    def accounts(self):
        return self._accounts

    def process_transactions(self):

        for acc in self.accounts:
            try:
                acc.deposit(1000)
                acc.withdraw(500)
            except Exception as e:
                print(e)

c = CurrentAC('123')
f = SavingsAC('234')
g = FDAC('456')

accounts = []
accounts.append(c)
accounts.append(f)
accounts.append(g)

user = Client(accounts)
user.process_transactions()
