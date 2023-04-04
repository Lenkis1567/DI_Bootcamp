# class Example:
#     """
#     Test for several functions
#     """
#     def __init__ (self, num):
#         pass
#     def abs(self, num):
#         return abs(num)
#     def int(self, num):
#         return int(num)
#     def input(self):
#         n = input("input something ")
#         return n

# num = Example(10)
# print(Example.__doc__)
# =============Currencies=============
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return (f"{str(self.amount)} {str(self.currency)}s")
    def __int__(self):
        return (self.amount)
    def __repr__(self):
        return repr(self.__str__())
    def __add_vall__(self, another_curr):
        if self.currency==another_curr.currency:
            return self.amount+another_curr.amount
        else:
            raise TypeError ("Cannot add between Currency type <dollar> and <shekel>")
    def __add_curr__(self, num):
        num1=int(num)
        return self.amount+num1
    def __mult_by__(self, num2):
        num_int=int(num2)
        self.amount+=num_int
        return self.amount
        # print(self.__str__())
    def __iadd__(self, another):
        if isinstance(another, int):
            self.amount+=another
            return self.amount
            print(self.amount__str__())
        else:
            if self.currency==another.currency:
                self.amount+=another.amount
                return self.amount
            else:
                raise TypeError ("Cannot add between Currency type <dollar> and <shekel>")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1.__str__())
print(c1.__int__())
print(c1.__repr__())
print(c1.__add_vall__(c2))
num = input("input a number: ")
num2 = int(num)
print(c1.__iadd__(num2))
print(c4.__iadd__(c3))
num1 = int(input("input a number: "))
c1.__iadd__ (num1)
print(c1.__str__())
# print(c4.__add_vall__(c2))