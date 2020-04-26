class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount


    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'r+') as file:
            file.write(str(self.balance))


class checking(Account):
    """This Class is for checking Account"""
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


account=checking('balance.txt',1)
account.transfer(100)
account.commit()
print(account.balance)
print(account.__doc__)

# account=Account('balance.txt')
# # print(account.withdraw(1000))
# print(account.deposit(1000))
# account.commit()
# print(account.balance)


