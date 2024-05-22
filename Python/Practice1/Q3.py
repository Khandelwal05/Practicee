class BankAccount:
    def __init__(self,account_number, account_holder, balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance= balance

    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance=self.balance - amount
        return self.balance
    
B1=BankAccount(123123, 'Riya', 1000)
a=B1.deposit(500)
b=B1.withdraw(1000)

print("Now the balance is ",b)
