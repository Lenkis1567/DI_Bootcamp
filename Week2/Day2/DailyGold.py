def print_cake(age:int) ->str:
    quant = 19 - 4 - age
    str1=' '*12+'_'*int((11-age)/2)+'i'*age+'_'*int((11-age)/2) 
    str='''
           |:H:a:p:p:y:|
         __|___________|__
        |^^^^^^^^^^^^^^^^^|
        |:B:i:r:t:h:d:a:y:|
        |                 |
        ~~~~~~~~~~~~~~~~~~~
        '''
    print(str1, end="")
    print(str)

date_birth=input("input your date of birth in format dd/mm/yy: ")
date_tuple = tuple(int(item) for item in date_birth.split('/'))
day_b=date_tuple[0]
month_b=date_tuple[1]
year_b=date_tuple[2]
current_date=(1, 4, 2023)
# print(day_b, month_b, year_b)
if month_b < current_date[1]:
    age_full = (2023-year_b)
if month_b > current_date[1]:
    age_full = ((2023-year_b)-1)
if month_b==current_date[1]:
    if day_b >current_date[0]:
        age_full = ((2023-year_b)-1)
    if day_b <= current_date[0]:
        age_full = (2023-year_b)
age=age_full%10
print_cake(age)
if year_b%4 ==0:
    print_cake(age)