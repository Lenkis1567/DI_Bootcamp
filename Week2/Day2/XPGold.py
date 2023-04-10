import string
import random
# =====1 Concatenate lists=======
list = [1, 2, 5, 9]
list1 = ['a', 'b', 'c', 'd']
for i in range(0, len(list1)):
    list.append(list1[i])
print(list)

# =====2 Range of numbers=======
list_num = []
for i in range(1500, 2500):
    if i%7==0 and i%5 ==0:
        list_num.append(i)
print(list_num)

# =====3 Check the index=======
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name_in = input("Please write a name: ")
if name_in in names:
    print("The index is ", names.index(name_in))

# =====4 Greatest Number=======
num1 = input("Please write the 1st number: ")
num1_int = int(num1)
num2 = input("Please write the 2nd number: ")
num2_int = int(num2)
num3 = input("Please write the 3rd number: ")
num3_int = int(num3)
list_num = [num1_int, num2_int, num3_int]
list_num.sort()
print("The greatest number is: ", list_num[-1])

# =====5 The Alphabet=======
string_alfa = "a b c d e f g h i g k l m n o p q r s t u v w x y z"
string_alfa.strip()
a=string_alfa.split()
print(a)
for letter in a:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        print(f'The letter {letter} is vowel')
    else:
        print(f'The letter {letter} is consonant')

# ============== Exercise 8 List and Tuple============
str_num = input("write numbers separated by the comma ")
str_num.strip()
b=str_num.split(",")
c = tuple(str_num.split(","))
print(b)
print (c)


# =====================Exercise 6: Words and letters=======================
word_list=[]
for a in range (0,6):
    word=input("please, write a word: ")
    word_list.append(word) 
letter=input("imput a letter: ")
places=[]
for i in range (0,6):
    if letter in word_list[i]:
        places.append(word_list[i])
        print(f"In the word {word_list[i]} the {letter} at the place #{word_list[i].find(letter)}")
    else:
        print(f'In the word {word_list[i]} there is no letter {letter}')
  
#=========================== Exercise 7:===================================
list_num=list(range(1,1000001))
# print( list_num)
# list_num=[]
# for i in range (0,1000000):
#     list_num.append(i+1)
min_l=min(list_num)
max_l=max(list_num)
sum_l = sum(list_num)
print(min_l, max_l, sum_l)
# ==================================Exercise 7 second version======================
list_num=[]
sum_l=0
min_l=1
max_l=1
for i in range (1,1000001):
    list_num.append(i)
    sum_l+=i
    if min_l>i:
        min_l=i
    if max_l<i:
        max_l=i
print(min_l, max_l, sum_l)


# #=========================== Exercise 9:===================================
win=0
loss=0
while True:
    numb_i=input("Input a random number from 1 to 9: ")
    if numb_i!="quit":
        numb_inp=int(numb_i)
        numb_my=random.randrange(1, 9)
        if numb_inp==numb_my:
            print('Winner!')
            win+=1
        else:
            print('better luck next time')
            loss+=1    
    else:
        print(f'Good buy! Total wins: {win}, total loss: {loss}')
        break

