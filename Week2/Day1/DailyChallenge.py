
a = input('Please write a string. The string must be 10 characters long: ')
letters = len(a)

if letters < 10:
    print ('string not long enough')
if letters > 10:
    print ('string too long')
if letters == 10:
    print ('great!')
    print(a[0])
    print(a[9]+ "       ")
for num in range(0, 10):
    print(a[num])
    num=num+1

import random
spisok = list(a)
print(spisok)
random.shuffle(spisok)
print(spisok)