class BankAccount:
    def __init__(self, username, password, balance, authenticated=False):
        self.balance=balance
        self.username=username
        self.password=password
        self.authenticated=authenticated
    def authenticate(self, username, password):
        if username==self.username and password==self.password:
            self.authenticated=True
    def deposit(self, sum):
        if self.authenticated==True:
            if sum<0:
                raise ValueError("The sum is not positive")
            else:
                self.balance+=sum
                return self.balance
        else:
            raise NameError("Password and username are not correct")
    def withdraw(self, minus):
        if self.authenticated==True:
            if sum<0:
                raise ValueError("The sum is not positive")
            else:
                self.balance-=minus
                if self.balance<0:
                    raise ValueError("The minimum sum at the account should be more than 0")
                else:
                    return self.balance
        else:
            raise NameError("Password and username are not correct")
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance, minimum_balance=0, authenticated=False):
        super().__init__(self, username, password, balance, authenticated)
        self.minimum_balance=minimum_balance

my=BankAccount("Developers", "Pass", 6000)

username=input("input the username: ")
password=input("input the password: ")
my.authenticate(username, password)
sum=int(input("Input a sum you wanna add to your account: "))
print(my.deposit(sum))
minus=int(input("Input a sum you wanna take from your account: "))
print(my.withdraw(minus))

# BONUS NOT DONE