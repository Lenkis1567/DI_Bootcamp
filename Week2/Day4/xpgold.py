# def get_age(year, month, day):
#     current_month=4
#     current_date=10
#     current_year=2023
#     if current_month>month:
#         age=current_year-year
#     else:
#         if current_month==month:
#             if current_date>=day:
#                 age=2023-year
#         else:
#             age=2023-year-1
#     return age
# print(get_age(1979,3,22))

# def can_retire(gender, date_of_birth):
#     print(date_of_birth)
#     month=date_of_birth[1]
#     day=date_of_birth[2]
#     year=date_of_birth[0]
#     age=get_age(year, month, day)
#     if gender=='female':
#         if age>62:
#             print("you can retire")
#         else:
#             print('you can not retire')
#     else:
#         if age>67:
#             print("you can reire")
#         else:
#             print('you can not retire')
# date_of_birth=[]
# date_of_birth.append(int(input("input your year of birth: ")))
# date_of_birth.append(int(input("input your month of birth: ")))
# date_of_birth.append(int(input("input your day of birth: ")))
# b=input("write your gender, male or female: ")
# can_retire(b, date_of_birth)


# # ++++++++++++++++++++++++++++++++++++++++++++throw_dice+++++++++++++++++++++

import random
def throw_dice():
    result=random.randint(1,6)
    return result
def throw_until_doubles():
    i=1
    while True:
        a=throw_dice()
        b=throw_dice()
        print(a,b)
        if a!=b:
            i=i+1
        else:
            break
    print(i)
    return i
throw_until_doubles()
def main():
    list_res=[]
    for a in range(1,100):
        throw_until_doubles()
        res=throw_until_doubles()
        list_res.append(res)
    return list_res
lis=main()
print(lis)
print("It took you", sum(lis), "tries to reach 100 doubles.")
print("Average throuws are: ", sum(lis)/100)