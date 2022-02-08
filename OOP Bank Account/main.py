# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
# and two methods:
#
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Added ${deposit_amount} to the balance.")

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f"Withdrawal accepted.")
        else:
            print('Sorry, not enough funds.')

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: ${self.balance}"


a = Account("Anastasia", 500)
print(a)
a.deposit(100)
print(a)
a.withdraw(600)
print(a)
a.withdraw(100)
print(a)

