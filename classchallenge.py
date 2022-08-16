from msilib.schema import Error


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

    def deposit(self,money):
        self.balance += money
        print("Deposit Accepted")

    def withdraw(self,money):
        if(self.balance >= money):
            self.balance -= money
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)