"""

                                    +-------------------------------------------------------- +
                                    |      Client                                             |
                                    +-------------------------------------------------------- +
                                    | - nonWithdrawableAccount : List<NonWithdrawableAccount> |
                                    | - withdrawableAccount : List<WithdrawableAccount>       |                                   
                                    |                                                         |
                                    +-------------------------------------------------------- +
                                        ▲          ▲
                                        |          |
                                        |          |
                +-----------------------------+    |
                | <<abstract>>                |    |
                | NonWithdrawableAccount      |    |
                +-----------------------------+    |
                | - accountNo                 |    |
                | - balance                   |    |
                +-----------------------------+    |
                | + deposit(amount)           |    |
                +-----------------------------+    |
                     ▲                 ▲           |
                     |                 |           |
                     |                 |           |
     +---------------------------+   +----------------------+
     | FixedDeposit (FD)         |   | <<abstract>>          |
     +---------------------------+   | WithdrawableAccount   |
                                     +----------------------+
                                     | + withdraw(amount)   |
                                     +----------------------+
                                          ▲          ▲
                                          |          |
                                     +-----------+  +------------+
                                     |  Savings  |  |  Current   |
                                     +-----------+  +------------+

"""

from abc import ABC , abstractmethod
from typing import List


class NonWithdrawableAccount:

    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    @abstractmethod
    def deposit(self, amount): ...

    @property
    def balance(self):
        return self._balance   

    @property
    def account_number(self):
        return self._account_number
    
class WithdrawableAccount(NonWithdrawableAccount):

    def __init__(self, account_number):
        super().__init__(account_number)

    @abstractmethod
    def withdraw(self, amount): ...


class SavingsAC(WithdrawableAccount):

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

class CurrentAC(WithdrawableAccount):

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


class FDAC(NonWithdrawableAccount):

    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        self._balance = self.balance + amount
        print(f"New balance after deposit {self.balance}")
    

class Client:

    def __init__(self, withdrawable_accounts: List[WithdrawableAccount], non_withdrawable_accounts: List[NonWithdrawableAccount]):
        self._withdrawable_accounts = withdrawable_accounts
        self._non_withdrawable_accounts = non_withdrawable_accounts

    @property
    def withdrawable_accounts(self):
        return self._withdrawable_accounts

    @property
    def non_withdrawable_accounts(self):
        return self._non_withdrawable_accounts
    
    def process_transactions(self):

        for acc in self.withdrawable_accounts:
            acc.deposit(1000)
            acc.withdraw(500)

        for acc in self.non_withdrawable_accounts:
            acc.deposit(1000)

c = CurrentAC('123')
s = SavingsAC('234')
f = FDAC('456')

withdrawable_accounts = []
withdrawable_accounts.append(c)
withdrawable_accounts.append(s)

non_withdrawable_accounts = []
non_withdrawable_accounts.append(f)

user = Client(withdrawable_accounts, non_withdrawable_accounts)
user.process_transactions()