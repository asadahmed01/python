from cmath import acos


class BankAccount:
    def __init__(self, accountNumber: int, name: str, balance: float):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient funds! your balance is $", self.balance)
        elif self.balance >= amount:
            self.balance -= amount


accnt = BankAccount(1122, "john", 100.00)
accnt.deposit(50.25)
print(accnt.balance)
accnt.withdraw(150)
print(accnt.balance)
