a = input('Please write a string. The string must be 10 characters long: ')
letters = len(a)

if letters < 10:
    print ('string not long enough')
if letters > 10:
    print ('string too long')
if letters == 10:
    print ('great! exactly 10 simbols')
    print ("First:", a[0])
    print ("Last:", a[9])

b=""
for num1 in range(0, 10):
    b=b+a[num1]
    print(b)
    num1=num1+1

import random
spisok = list(a)
print(spisok)
random.shuffle(spisok)
spisok1=''.join(spisok)
print(spisok1)