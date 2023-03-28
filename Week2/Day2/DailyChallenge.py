number = input("Please, insert a number ")
number_int=int(number)
n = 1
length = input ("Please, insert a length ")
length_int=int(length)
for n in range(1, length_int+1):
    print(number_int*n)
    n=n+1
