import string
# # =====Concatenate lists=======
# list = [1, 2, 5, 9]
# list1 = ['a', 'b', 'c', 'd']
# for i in range(0, len(list1)):
#     list.append(list1[i])
# print(list)
# # =====Range of numbers=======
# list_num = []
# for i in range(1500, 2500):
#     if i%7==0 and i%5 ==0:
#         list_num.append(i)
# print(list_num)
# =====Check the index=======
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# name_in = input("Please write a name: ")
# if name_in in names:
#     print("The index is ", names.index(name_in))
# =====Greatest Number=======
# num1 = input("Please write the 1st number: ")
# num1_int = int(num1)
# num2 = input("Please write the 2nd number: ")
# num2_int = int(num2)
# num3 = input("Please write the 3rd number: ")
# num3_int = int(num3)
# list_num = [num1_int, num2_int, num3_int]
# list_num.sort()
# print("The greatest number is: ", list_num[-1])
# # =====The Alphabet=======
# string_alfa = "a b c d e f g h i g k l m n o p q r s t u v w x y z"
# string_alfa.strip()
# a=string_alfa.split()
# print(a)
# for letter in a:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
#         print(f'The letter {letter} is vowel')
#     else:
#         print(f'The letter {letter} is consonant')

# ============== List and Tuple============
str_num = input("write numbers separated cy the comma ")
str_num.strip()
b=str_num.split(",")
c = tuple(str_num.split(","))
print(b)
print (c)
