# 1. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the
# perimeter of a circle.


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 3.14 * self.radius * 2


circle = Circle(7)
print(f"Area is {circle.area()}. \nPerimeter is {circle.perimeter()}")


'''
2. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether 
they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in 
object class or not.
'''


class Student:
    pass


class Marks:
    pass


student = Student()
mark = Marks()

print(f"student is instance of class Student : {isinstance(student, Student)}. \n")
print(f"mark is instance of class Student : {isinstance(mark, Student)}. \n")


'''
------------A Bank------------

A. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. A 
SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a 
method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account object, 
should have an overdraft limit attribute.

B. Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be 
instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some 
of each type).

C. Write an update method in the Bank class. It iterates through each account, updating it in the following ways: 
Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they are 
in overdraft. (use print to 'send' the letter).

D. The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.
'''

#A


class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        self.deposit(self.interest)
        print(f"Account {self.get_account_number()} has {self.get_balance()} money")


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft):
        super().__init__(balance, account_number)
        self.overdraft = overdraft

    def send_letter(self):
        if self.overdraft > self.get_balance():
            print(f"Account {self.get_account_number()} is in debt")


#B


class Bank:
    def __init__(self, accounts: list):
        self.accounts = accounts

    def account_check(self):
        for acc in self.accounts:
            if isinstance(acc, SavingsAccount):
                acc.add_interest()
            if isinstance(acc, CurrentAccount):
                acc.send_letter()

    def open_account(self, account: Account):
        self.accounts.append(account)

    def close_account(self, account: Account):
        self.accounts.remove(account)

    def pay_dividents(self):
        for acc in self.accounts:
            acc.deposit(1)


baseAccount = Account(0, 1)
interestAccount = SavingsAccount(100, 2, 1)
currentAccount = CurrentAccount(120, 3, 123)

bank = Bank([baseAccount, interestAccount, currentAccount])


#C
bank.account_check()

#D
my_account = CurrentAccount(0, 11, 0)
bank.open_account(my_account)
print(f"My account {my_account.get_account_number()} has {my_account.get_balance()} money")
bank.pay_dividents()
print(f"My account {my_account.get_account_number()} has {my_account.get_balance()} money")
bank.close_account(my_account)
bank.pay_dividents()
print(f"My account {my_account.get_account_number()} has {my_account.get_balance()} money")
