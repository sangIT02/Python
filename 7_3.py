from abc import  ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, money):
        pass

    @abstractmethod
    def withdraw(self, money):
        pass

    @abstractmethod
    def get_balane(self):
        pass

class SavingAccount(Account):
    def __init__(self ):
        self.balance = 0

    def get_balane(self):
        return self.balance

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            print(f"Da rut thanh cong {money} vnd, so du con lai: {self.balance} vnd")
        else:
            print("so tien rut khong hop le hoac so du khong du, vui long thu lai sau!")

    def deposit(self, money):
        if money <= 0:
            print("so tien gui khong hop le, vui long hay thu lai!")
        else:
            self.balance += money
            print(f"So du sau khi gui la: {self.balance} vnd")

class CheckingAccount(Account):
    def __init__(self, limit = 10000):
        self.balance = 0
        self.limit = limit

    def get_balane(self):
        return self.balance
    def withdraw(self, money):
        if money > 0 and (self.balance - money) >= -self.limit:
            self.balance -= money
            print(f"Da rut thanh cong {money} vnd, so du con lai: {self.balance} vnd")
        else:
            print("so tien rut khong hop le hoac so du khong du, vui long thu lai sau!")

    def deposit(self, money):
        if money <= 0:
            print("so tien gui khong hop le, vui long hay thu lai!")
        else:
            self.balance += money
            print(f"So du sau khi gui la: {self.balance} vnd")

sc = SavingAccount()
sc.deposit(10000)
sc.withdraw(500)

cc = CheckingAccount()
cc.deposit(20000)
cc.withdraw(25000)
