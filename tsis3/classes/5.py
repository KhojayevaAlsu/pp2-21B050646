'''Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.'''


class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, dep_sum):
        self.balance += dep_sum
        print("Deposit has been accepted")



    def withdraw(self,withdraw_sum):
        if self.balance >= withdraw_sum:
            self.balance -= withdraw_sum
            print("Withdraw has been accepted")
        else:
            print("Withdraw has not been accepted")
    def print(self) :
        print(self.balance)


owner_name = input() 
balance = float(input())
n = Account(owner_name,balance)
dep_sum = int(input())
n.deposit(dep_sum)
withdraw_sum = int(input())
n.withdraw(withdraw_sum)
