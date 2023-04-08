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
# n=0
# topping_list = []
# topping = ''
# topping = input("please write your favourite pizza topping or quit: ")
# while topping != "quit":
#     print("Ok, we will add the", topping)
#     topping_list.append(topping)
#     topping = input("please write your favourite pizza topping or quit: ")
#     n=n+1

# print ("Your toppings are:", topping_list)
# price = 10+n*2.5
# print ("The price is:", price)

# # --------------------9------------------------

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



# #--------------------9 add------------------------
# # eligable = []
# teenagers = ["Ron", "John", "Mary", "Bill"]
# teenagers_info = []
# ages = []
# for teenager in teenagers:
#     age = input(f"Hi, {teenager}, Tell me your age: ")
#     age_int = int(age)
#     info = (teenager, age_int)
#     teenagers_info.append(info)
# permitted = []
# for name, age in teenagers_info:
#     if age > 16 and age< 21:
#         continue
#     else:
#         permitted.append(name)

# print(teenagers_info)
# print("They can enter:", permitted)

# ===============Sandwich Orders==========================
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders_without_p=[]
finished_sandwiches = []
print("Sorry, we ran our of pastrami, so today no sandwiches with it. We will remove them from our menu, you can try those:")
for b in range(0,len(sandwich_orders)):
    if sandwich_orders[b]!="Pastrami sandwich":
        sandwich_orders_without_p.append(sandwich_orders[b])
print(sandwich_orders_without_p)
for n in range(0, len(sandwich_orders_without_p)):
    a = input(f'Is the {sandwich_orders_without_p[n]} is done? Print Yes, if so, else print No ')
    ap=a.upper()
    if ap == "YES":
         finished_sandwiches.append(sandwich_orders_without_p[n])

for i in range(0, len(finished_sandwiches)):
    if finished_sandwiches!=[]:
        print(f'I"ve done your {finished_sandwiches[i]}')
    else:
        print("Nothing for you today")    
