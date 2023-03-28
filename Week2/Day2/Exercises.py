# # -------------------1----------------
# my_fav_numbers = {5, 7, 11, 13, 27} 
# my_fav_numbers.add(21)
# my_fav_numbers.add(101)
# print(my_fav_numbers)
# my_fav_numbers.remove(101)
# print(my_fav_numbers)
# friend_fav_numbers = {6, 3, 8, 17, 23, 105, 7}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # -------------------2---------------
# int_tuple= (1, 2, 3)
# int_tuple_list = list (int_tuple)
# print(int_tuple_list)
# int_tuple_list.append (8)
# print(int_tuple_list) 
# # we can add it only if we make list out of tuple

# #--------------------3------------------------
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# del basket [-1]
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apple")
# print(basket)
# del basket [0:5]
# print(basket)

# #--------------------4------------------------
# flo_list =[]
# for n in range(3,11):
#     flo = [n/2]
#     flo_list.insert(n-3, flo) 
    
# print(flo_list)
# #--------------------5------------------------
# for num in range(1,21):
#     print(num)
# set=-===========================

# list = []
# a1 = 1
# for num in range(1, 21):
#     list.append(num)
# print(list)
# for num1 in range(1, 11):
#     print (list[a1])
#     a1 = a1+2
# #--------------------6------------------------

# while True:
#     a = input('Please, tell me your name: ')
#     if a == "Elena":
#          break
#     else:
#         continue 

# #--------------------7------------------------
# fruits = input("please write what your favourite fruits, separate them with space: ")
# fruits_st = fruits.split ()
# any_fruit = input("please write a fruit name: ")
# if any_fruit in fruits_st:
#     print("It' your favourite, enjoy!")
# else: 
#     print ("You've chosen another fruit")
#     #--------------------8------------------------
n=0
topping_list = []
topping = ''
topping = input("please write your favourite pizza topping or quit: ")
while topping != "quit":
    print("Ok, we will add the", topping)
    topping_list.append(topping)
    topping = input("please write your favourite pizza topping or quit: ")
    n=n+1

print ("Your toppings are:", topping_list)
price = 10+n*2.5
print ("The price is:", price)

# --------------------9------------------------

# age_list = []
# num_fam = 0
# price = 0
# quantity_members = input('Please, tell me how many are you: ')
# quantity_members_int = int(quantity_members)
# while num_fam < quantity_members_int:
#     age = input('Please, tell me how old are you: ')
#     age_int = int(age)
#     if age_int > 3 and age_int <12 : 
#         price = price + 10
#     if age_int > 13:
#         price = price + 15
#     num_fam = num_fam+1
# print("You will have to pay: ", price)



# #--------------------10------------------------
# final_list = []
# teenagers = input("please write your names, separate them with space: ")
# teenagers_st = teenagers.split ()
# print (teenagers_st)
# num11 = len(teenagers_st)
# print (num11)
# for n in range (0, num11+1):
#     current_name = teenagers_st[n]
#     print (current_name, ",")
#     age = input("Tell me your age: ",)
#     age_int = int(age)
#     if age_int < 16 or age_int > 21:
#         final_list.append(current_name)

# print(final_list)